from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('services/', views.ListServices.as_view(), name='list_service'),
    path('services/<str:service_type>/', views.DetailService.as_view(), name='detail_service'),
    path('majors/', views.ListMajors.as_view(), name='list_majors'),
    path('majors/<str:major_code>/', views.DetailMajor.as_view(), name='detail_major'),
    path('classes/', views.ListClasses.as_view(), name='list_classes'),
    path('classes/<str:class_code>/', views.DetailClass.as_view(), name='detail_class'),
    # path('classes/<str:school>/', views.ListClassesBySchool.as_view(), name='classes_by_school_list'),
    path('schools/', views.ListSchools.as_view(), name='list_schools'),
    path('schools/<str:school_code>/', views.DetailSchool.as_view(), name='detail_school'),
]
