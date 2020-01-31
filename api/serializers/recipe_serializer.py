from rest_framework import serializers

from domain.models import Recipe
from api.serializers.photo_serializer import PhotoSerializer
from api.serializers.step_serializer import StepSerializer


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'main_image']


class RecipeDetailSerializer(serializers.ModelSerializer):
    steps = StepSerializer(source='get_steps', read_only=True, many=True)
    photos = PhotoSerializer(source='get_photos', read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'main_image', 'time_to_make', 'level', 'create_date', 'user_id', 'steps', 'photos']


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'main_image', 'time_to_make', 'level', 'user']


class RecipeUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'main_image', 'time_to_make', 'level', 'user_id']
