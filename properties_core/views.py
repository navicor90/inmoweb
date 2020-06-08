from django.contrib.auth.models import User, Group
from properties_core.models import Property
from rest_framework import viewsets
from properties_core.serializers import UserSerializer, GroupSerializer, PropertySerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@method_decorator(login_required, name='dispatch')
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@method_decorator(login_required, name='dispatch')
class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

