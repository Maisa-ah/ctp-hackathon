from django.shortcuts import render

from django.shortcuts import get_object_or_404
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
        services = models.Service.objects.filter(service_type=service_type)
        serializer = serializers.ServiceSerializer(services, many=True)
        return Response(serializer.data)


class ListMajors(APIView):
    def get(self, request, format=None):
        majors = models.Major.objects.all()
        serializer = serializers.MajorSerializer(majors, many=True)
        return Response(serializer.data)


class MajorDetail(APIView):
    def get_object(self, major_code):
        return get_object_or_404(Major, major_code=major_code)

    def get(self, request, major_code, format=None):
        major = self.get_object(major_code)
        serializer = serializers.MajorSerializer(major)
        return Response(serializer.data)

    def put(self, request, major_code, format=None):
        major = self.get_object(major_code)
        serializer = serializers.MajorSerializer(major, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, major_code, format=None):
        major = self.get_object(major_code)
        major.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetMajorbyMajorCode(APIView):
    def get(self, request, format=None):
        major_code = request.data['major_code']
        major = get_object_or_404(Major, major_code=major_code)
        serializer = serializers.MajorSerializer(major, many=False)
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
        serializer = serializers.ClassSerializer(classes)


class ClassDetail(APIView):
    def get_object(self, class_code):
        return get_object_or_404(Class, class_code=major_code)

    def get(self, request, class_code, format=None):
        this_class = self.get_object(major_code)
        serializer = serializers.ClassSerializer(this_class)
        return Response(serializer.data)

    def put(self, request, class_code, format=None):
        this_class = self.get_object(class_code)
        serializer = serializers.ClassSerializer(this_class, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, class_code, format=None):
        this_class = self.get_object(class_code)
        this_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListSchools(APIView):
    def get(self, request, format=None):
        schools = models.School.objects.all()
        serializer = serializers.SchoolSerializer(classes, many=True)
        return Response(serializer.data)
