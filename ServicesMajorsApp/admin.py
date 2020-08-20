from django.contrib import admin

from .models import Class, Major, Service, School

admin.site.register(Class)
admin.site.register(Major)
admin.site.register(Service)
admin.site.register(School)
