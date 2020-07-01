from django.contrib.auth.models import User, Group
from properties_core.models import Property
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['ref_id',
                  'district',
                  'province',
                  'currency',
                  'amount',
                  'price',
                  'url',
                  'source_web',
                  'scrapped_date',
                  'description',
                  'extra_json_info',
                  'property_type']
        validators = [
            UniqueTogetherValidator(
                queryset=Property.objects.all(),
                fields=['ref_id', 'source_web']
            )
        ]
