from django.contrib.auth import authenticate, login as auth_login, logout as logout_auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
from domain.models import Recipe, Photo
from website.decorators import unauthenticated_only
from website.forms import LoginForm, RegisterForm


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
    photos = Photo.objects.filter(recipe_id=id)
    context = {
        'recipe': recipe,
        'photos': photos
    }
    return HttpResponse(template.render(context, req))


@unauthenticated_only
def login(req):
    error = None
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user is not None:
                auth_login(req, user)
                return HttpResponseRedirect('/')
            else:
                error = 'Niepoprawne dane logowania!'
    template = loader.get_template('login.html')
    context = {
        'error': error
    }
    return HttpResponse(template.render(context, req))


@unauthenticated_only
def register(req):
    error = None
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    User.objects.create_user(username=username, password=password)
                    return HttpResponseRedirect('/login/')
                except:
                    error = 'Login jest już w użyciu'
            else:
                error = 'Hasła nie są takie same'
        else:
            error = 'Zweryfikuj dane'
    template = loader.get_template('register.html')
    context = {
        'error': error
    }
    return HttpResponse(template.render(context, req))


def logout(req):
    logout_auth(req)
    return HttpResponseRedirect('/login/')


def notfound(req):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
