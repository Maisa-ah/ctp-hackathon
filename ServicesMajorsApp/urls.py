from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('services/', views.ListServices.as_view(), name='service_list'),
    path('services/<str:service_type>',
         views.ListServicesByType.as_view(), name='service_by_type_list'),
    path('majors/', views.ListMajors.as_view(), name='majors_list'),
    path('classes/', views.ListClasses.as_view(), name='classes_list'),
    path('classes/<str:school>', views.ListClassesBySchool.as_view(),
         name='classes_by_school_list'),
    path('schools/', views.ListSchools.as_view(), name='schools_list'),
    path('majors/<str:major_code>', views.GetMajorbyMajorCode.as_view(),
         name='major_by_major_code')
=======
    path('services/', views.ListServices.as_view(), name='list_service'),
    path('services/<str:service_type>/', views.DetailService.as_view(), name='detail_service'),
    path('majors/', views.ListMajors.as_view(), name='list_majors'),
    path('majors/<str:major_code>/', views.DetailMajor.as_view(), name='detail_major'),
    path('classes/', views.ListClasses.as_view(), name='list_classes'),
    path('classes/<str:class_code>/', views.DetailClass.as_view(), name='detail_class'),
    # path('classes/<str:school>/', views.ListClassesBySchool.as_view(), name='classes_by_school_list'),
    path('schools/', views.ListSchools.as_view(), name='list_schools'),
    path('schools/<str:school_code>/', views.DetailSchool.as_view(), name='detail_school'),
>>>>>>> ce8f96db0b9544db13a62a0ee268c62a15997be2
]
