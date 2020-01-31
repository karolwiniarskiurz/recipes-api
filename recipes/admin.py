from django.contrib import admin

# Register your models here.
from domain.models import Recipe

admin.site.register(Recipe)
