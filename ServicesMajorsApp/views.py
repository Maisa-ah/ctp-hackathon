from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class ListServices(APIView):
    def get(self, request, format=None):
        services = models.Service.objects.all()
        serializer = serializers.ServiceSerializer(services, many=True)
        return Response(serializer.data)


class ListServicesByType(APIView):
    def get(self, request, format=None):
        service_type = request.data['service_type']
        services = models.Service.objects.filter(service_type=service_type]
        serializer = serializers.ServiceSerializer(services, many=True)
        return Response(serializer.data)


class ListMajors(APIView):
    def get(self, request, format=None):
        majors = models.Major.objects.all()
        serializer = serializers.MajorSerializer(majors, many=True)
        return Response(serializer.data)


class ListClasses(APIView):
    def get(self, request, format=None):
        clasess = models.Class.objects.all()
        serializer = serializers.ClassSerializer(classes, many=True)
        return Response(serializer.data)


class ListClassesBySchool(APIView):
    def get(self, request, format=None):
        school = request.data['school']
        classes = models.Class.objects.filter(school=school)
        serializer = serializers.ClassSerializer(classes, many=True)


class ListSchools(APIView):
    def get(self, request, format=None):
        schools = models.School.objects.all()
        serializer = serializers.SchoolSerializer(classes, many=True)
        return Response(serializer.data)
