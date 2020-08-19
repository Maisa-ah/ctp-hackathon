from rest_framework import viewsets, generics, views, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserSerializer, LoginSerializer, RegisterSerializer
from .models import Profile
  
class UserViewSet(viewsets.ModelViewSet): 
    queryset = Profile.objects.all() 
    serializer_class = UserSerializer

class ProfileAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(Profile, pk=kwargs['user_id'])
        profile_serializer = UserSerializer(user)
        return Response(profile_serializer.data)

class UserProfile(views.APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        profile_serializer = UserSerializer(user.profile)
        return Response(profile_serializer.data)
    
    def put(self, request, format=None):
        profile = self.get_object(self.request.user.profile.pk)
        serializer = UserSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.RetrieveAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    error_messages = {
        'invalid': "Invalid username or password",
    }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_100_OK)
        return self._error_response('invalid')