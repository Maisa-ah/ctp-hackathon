from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    fields = ('user', 'current_year', 'date_of_birth', 'bio')

admin.site.register(Profile, ProfileAdmin)