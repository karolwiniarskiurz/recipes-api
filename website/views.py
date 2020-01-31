from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

# Create your views here.
from domain.models import Recipe, RecipeStep, Photo


def index(req):
    last_recipes = Recipe.objects.order_by('create_date')[:3]
    context = {
        'last_recipes': last_recipes
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, req))


def search(req):
    query = req.GET['query']
    if query is None or len(query) == 0:
        return HttpResponseRedirect('/')

    template = loader.get_template('search.html')
    recipes = Recipe.objects.all().filter(name__contains=query)
    context = {
        'query': query,
        'recipes': recipes
    }
    return HttpResponse(template.render(context, req))


def detail(req, id):
    try:
        recipe = Recipe.objects.get(id=id)
    except:
        return HttpResponseRedirect('/404')
    template = loader.get_template('detail.html')
    steps = RecipeStep.objects.filter(recipe_id=id).order_by('no')
    photos = Photo.objects.filter(recipe_id=id)
    context = {
        'recipe': recipe,
        'steps': steps,
        'photos': photos
    }
    return HttpResponse(template.render(context, req))


def notfound(req):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
