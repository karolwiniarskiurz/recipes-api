from django.contrib import admin

# Register your models here.
from recipes.api.models import Recipe

admin.site.register(Recipe)
