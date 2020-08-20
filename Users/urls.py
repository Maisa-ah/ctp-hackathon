from django.urls import path, include
from .views import UserViewSet, ProfileAPI, UserProfile
from rest_framework.routers import DefaultRouter

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('profile/', UserProfile.as_view()),
    path('profile/<int:user_id>/', ProfileAPI.as_view()),
]
