from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    LEVEL = [
        ('VE', 'Bardzo łatwe'),
        ('E', 'Łatwe'),
        ('M', 'Średnie'),
        ('H', 'Trudne'),
        ('VH', 'Bardzo trudne')
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=50000)
    steps = models.CharField(max_length=50000)
    main_image = models.CharField(max_length=500)
    time_to_make = models.CharField(max_length=100)
    level = models.CharField(max_length=2, choices=LEVEL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def get_photos(self):
        photos = Photo.objects.filter(recipe=self)
        return photos


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=1000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

