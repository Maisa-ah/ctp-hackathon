from rest_framework import viewsets 
from .serializers import UserSerializer
from .models import Profile

  
class UserViewSet(viewsets.ModelViewSet): 
    queryset = Profile.objects.all() 
    serializer_class = UserSerializer

