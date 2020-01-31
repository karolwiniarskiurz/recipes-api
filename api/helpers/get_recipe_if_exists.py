from django.http import Http404

from domain.models import Recipe


def get_recipe_if_exists(id):
    try:
        return Recipe.objects.get(pk=id)
    except Recipe.DoesNotExist:
        raise Http404
