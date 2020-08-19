from rest_framework import serializers

from . import models


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('class_code', 'class_name')
        model = models.Class


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('major_code', 'major_title')
        model = models.Major


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('school_code', 'school_name')
        model = models.School


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('service_type',)
        model = models.Service
