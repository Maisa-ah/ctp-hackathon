from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile

class UserSerializer(serializers.ModelSerializer):

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