from django.contrib.auth.models import User, Group
from properties_core.models import Property
from rest_framework import viewsets, status
from properties_core.serializers import UserSerializer, GroupSerializer, PropertySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
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


@api_view(['POST'])
def properties_batch(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        if isinstance(request.data, list) and len(request.data) <= 20:
            properties = request.data
            serializers = []
            all_duplicated = True
            errors = []
            for p in properties:
                s = PropertySerializer(data=p)
                if s.is_valid():
                    serializers.append(s)
                    all_duplicated = False
                elif 'non_field_errors' in s.errors.keys():
                    # Duplicated case
                    all_duplicated &= all_duplicated
                    errors.append(s.errors)
                else:
                    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

            if all_duplicated:
                return Response(errors, status=status.HTTP_409_CONFLICT)

            resp_data = []
            for s in serializers:
                s.save()
                resp_data.append(s.data)
            return Response(resp_data, status=status.HTTP_201_CREATED)
        else:
            return Response("This endpoint receive a list with 20 elements or less.", status=status.HTTP_400_BAD_REQUEST)
