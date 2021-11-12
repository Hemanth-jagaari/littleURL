from django.contrib import admin

# Register your models here.
from django.apps import apps
from .models import URLmap
admin.site.register(URLmap)
