from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Service, School, Major, Class
from .serializers import ServiceSerializer, MajorSerializer, SchoolSerializer, ClassSerializer, MatchSerializer

from .utils import mapper


class ListServices(APIView):
    def get(self, request, format=None):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class DetailService(APIView):
    def get_object(self, service_code):
        try:
            return Service.objects.get(service_code=service_code)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, service_code, format=None):
        service = self.get_object(service_code)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)



class ListMajors(APIView):
    def get(self, request, format=None):
        majors = Major.objects.all()
        serializer = MajorSerializer(majors, many=True)
        return Response(serializer.data)

class DetailMajor(APIView):
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


class ListClasses(APIView):
    def get(self, request, format=None):
        query_param = self.request.query_params.get('school', None)
        if query_param:
            schools = Class.objects.filter(school=query_param)
        else:
            classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

class DetailClass(APIView):
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


# Incredibly fucking ugly logic

class Matcher(APIView):
    def get(self, request, format=None):
        """
        Sample data form:

        { 'data': {
            'service': 'Career',
            'school_only': False,
            'user': {
                'school': 'Baruch',
                'classes': ['CIS2300', 'CIS3400'],
                'major': 'CIS'
                }
            }
        }

        """

        from Users.models import Profile

        # This should come from the frontend 
        data = {
            'service': 'Career',
            'school_only': False,
            'user': {
                'id': 1,
                'school': 'Baruch',
                'classes': ['CIS2300', 'CIS3400'],
                'major': 'CIS'
                }
            }
        
        service = data['service']
        school_only = data['school_only']
        user = data['user']


        # Query for users depending on user's preference
        if school_only:            
            users = Profile.objects.filter(school__school_code=user.school).exclude(user=user['id']).filter(services=service)
        else:
            users = Profile.objects.exclude(user=user['id']).filter(services=service)
        
        # Iterate over users and calculate the "matching" score
        matches = []
        for u in users.iterator():
            matches.append(mapper(service, user, u))

        if not matches:
            return Response({})

        serializer = MatchSerializer(matches, many=True)

        return Response(serializer.data)


