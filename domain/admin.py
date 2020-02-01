from django.contrib import admin

# Register your models here.
from domain.models import Recipe, Photo

admin.site.register(Recipe)
admin.site.register(Photo)
