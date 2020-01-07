from rest_framework import serializers

from recipes.api.models import Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['link']


class PhotoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['link', 'recipe']
