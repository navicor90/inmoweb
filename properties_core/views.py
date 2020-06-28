from django.contrib.auth.models import User, Group
from properties_core.models import Property
from rest_framework import viewsets, status
from properties_core.serializers import UserSerializer, GroupSerializer, PropertySerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]  
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows properties to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def create(self, request):
        data = json.loads(request.body.decode("utf-8"))
        if 'ref_id' in data.keys() and 'source_web' in data.keys():
            props = Property.objects.filter(ref_id=data['ref_id']) \
                                    .filter(source_web=data['source_web'])
            if len(props) > 0:
                return Response(data={"reason": "Object already exists"}, status=status.HTTP_409_CONFLICT)
        return super().create(request)
