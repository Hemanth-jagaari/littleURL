from django.contrib import admin

# Register your models here.
from django.apps import apps
from .models import URLmap
from .models import URLmanage
admin.site.register(URLmap)
admin.site.register(URLmanage)
