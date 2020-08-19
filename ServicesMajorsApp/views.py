from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Service, School, Major, Class
from .serializers import ServiceSerializer, MajorSerializer, SchoolSerializer, ClassSerializer


class ListServices(APIView):
    def get(self, request, format=None):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class DetailService(APIView):
    def get_object(self, service_type):
        try:
            return Service.objects.get(service_type=service_type)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, service_type, format=None):
        service = self.get_object(service_type)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)


class ListMajors(APIView):
    def get(self, request, format=None):
        majors = Major.objects.all()
        serializer = MajorSerializer(majors, many=True)
        return Response(serializer.data)


class DetailMajor(APIView):
    def get_object(self, major_code):
        try:
            return Major.objects.get(major=major_code)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, major_code, format=None):
        major = self.get_object(major_code)
        serializer = MajorSerializer(major)
        return Response(serializer.data)


class ListClasses(APIView):
    def get(self, request, format=None):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class DetailClass(APIView):
    def get_object(self, class_code):
        try:
            return Class.objects.get(class_code=class_code)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, class_code, format=None):
        _class = self.get_object(class_code)
        serializer = MajorSerializer(_class)
        return Response(serializer.data)


# class ListClassesBySchool(APIView):
#     def get(self, request, format=None):
#         school = request.data['school']
#         classes = Class.objects.filter(school=school)
#         serializer = ClassSerializer(classes, many=True)


class ListSchools(APIView):
    def get(self, request, format=None):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

class DetailSchool(APIView):
    def get_object(self, school_code):
        try:
            return School.objects.get(school_code=school_code)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, school_code, format=None):
        school = self.get_object(school_code)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)