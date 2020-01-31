from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.helpers.add_related_data_to_recipe import add_related_data_to_recipe
from api.helpers.get_user_by_username import get_user_by_username_from_headers
from api.helpers.is_authenticated import is_authenticated_headers
from domain.models import Recipe
from api.serializers.photo_serializer import PhotoCreateSerializer
from api.serializers.recipe_serializer import RecipeSerializer, RecipeCreateSerializer
from api.serializers.step_serializer import StepCreateSerializer


class RecipeListView(APIView):

    def build_fiters(self, params, possible_filters):
        filters = {}
        for filter in possible_filters:
            filter_name = filter['name']
            param = params.get(filter_name)
            if param:
                # if search if fuzzy it will search with link not with where
                filters[filter_name if filter['fuzzy'] is False else f'{filter_name}__contains'] = param
        return filters

    def get(self, req):
        possible_filters = [{'name': 'name', 'fuzzy': True}, {'name': 'level', 'fuzzy': False}]
        filters = self.build_fiters(req.GET, possible_filters)

        recipes = Recipe.objects.filter(**filters).order_by('create_date')
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, req):
        if not is_authenticated_headers(headers=req.META):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # adding recipe
        user = get_user_by_username_from_headers(req.META)
        data = req.data
        data['user'] = user.id
        serializer = RecipeCreateSerializer(data=data)
        if serializer.is_valid():
            recipe = serializer.save()
            recipe_id = recipe.id
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        # adding steps
        try:
            add_related_data_to_recipe(req.data['steps'], StepCreateSerializer, recipe_id)
        except Exception as e:
            return Response(str(e), status.HTTP_400_BAD_REQUEST)

        # adding photos
        try:
            add_related_data_to_recipe(req.data['photos'], PhotoCreateSerializer, recipe_id)
        except Exception as e:
            return Response(str(e), status.HTTP_400_BAD_REQUEST)

        return Response(recipe_id, status=status.HTTP_201_CREATED)
