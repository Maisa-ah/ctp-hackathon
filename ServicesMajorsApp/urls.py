from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListServices.as_view(), name='service_list'),
    path('', views.ListServicesByType.as_view(), name='service_by_type_list'),
    path('', views.ListMajors.as_view(), name='majors_list'),
    path('', views.ListClasses.as_view(), name='classes_list'),
    path('', views.ListClassesBySchool.as_view(), name='classes_by_schoo_list'),
    path('', views.ListSchools.as_view(), name='schools_list'),
]
