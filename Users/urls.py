from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include('allauth.urls')),
    path('', include(router.urls)),
]
