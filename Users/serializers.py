from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class UserSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
