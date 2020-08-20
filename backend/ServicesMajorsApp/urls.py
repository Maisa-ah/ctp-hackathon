from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('services/', views.ListServices.as_view(), name='list_service'),
    path('services/<str:service_code>',
         views.DetailService.as_view(), name='detail_service'),
    path('majors/', views.ListMajors.as_view(), name='list_majors'),
    path('majors/<str:major_code>/', views.DetailMajor.as_view(), name='detail_majors'),
    path('classes/', views.ListClasses.as_view(), name='list_classes'),
    path('classes/<str:class_cpde>', views.DetailClass.as_view(),
         name='detail_class'),
    path('schools/', views.ListSchools.as_view(), name='list_schools'),
    path('schools/<str:school_code>', views.DetailSchool.as_view(), name='detail_school'),
    path('match/', views.Matcher.as_view(), name='matcher')
]
