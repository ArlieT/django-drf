from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Test

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='user-details',  # Replace with the actual view name for your UserViewSet
        lookup_field='pk'
    )
    class Meta:
        model = User
        # fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'
# 


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        # fields = ['url', 'name']
        fields = '__all__'
        
        

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

    