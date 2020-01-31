from rest_framework import serializers

from domain.models import RecipeStep


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ['no', 'text']


class StepDetailSerializer(serializers.ModelSerializer):
    model = RecipeStep
    fields = '__all__'


class StepCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ['no', 'text', 'recipe']
