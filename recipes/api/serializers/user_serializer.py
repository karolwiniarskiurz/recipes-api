from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=64)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8, max_length=128)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
