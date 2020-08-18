from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('services/', views.ListServices.as_view(), name='service_list'),
    path('services/<str:service_type>',
         views.ListServicesByType.as_view(), name='service_by_type_list'),
    path('majors/', views.ListMajors.as_view(), name='majors_list'),
    path('classes/', views.ListClasses.as_view(), name='classes_list'),
    path('classes/<str:school>', views.ListClassesBySchool.as_view(),
         name='classes_by_school_list'),
    path('schools/', views.ListSchools.as_view(), name='schools_list'),
]
