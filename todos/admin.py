from django.contrib import admin

from .models import Todo,UserProfile,Domain

admin.site.register(Todo)
admin.site.register(UserProfile)
admin.site.register(Domain)