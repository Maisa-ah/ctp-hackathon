from rest_framework import serializers

from .models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'current_year', 'date_of_birth', 'bio']
