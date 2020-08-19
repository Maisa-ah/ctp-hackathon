from django.shortcuts import render

from django.shortcuts import get_object_or_404
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
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class ListClassesBySchool(APIView):
    def get(self, request, format=None):
        school = request.data['school']
        classes = models.Class.objects.filter(school=school)
        serializer = serializers.ClassSerializer(classes)


# class ClassDetail(APIView):
#     def get_object(self, class_code):
#         return get_object_or_404(Class, class_code=major_code)

#     def get(self, request, class_code, format=None):
#         this_class = self.get_object(major_code)
#         serializer = serializers.ClassSerializer(this_class)
#         return Response(serializer.data)

#     def put(self, request, class_code, format=None):
#         this_class = self.get_object(class_code)
#         serializer = serializers.ClassSerializer(this_class, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, class_code, format=None):
#         this_class = self.get_object(class_code)
#         this_class.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

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
