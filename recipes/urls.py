"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from recipes.api.views.login_view import LoginView
from recipes.api.views.user_view import UserViewSet
from recipes.api.views.group_view import GroupViewSet
from recipes.api.views.recipe_detail_view import RecipeDetailView
from recipes.api.views.recipe_list_view import RecipeListView
from recipes.api.views.register_view import RegisterView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# todo: add admin

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('recipes/<int:id>/', RecipeDetailView.as_view()),
    path(r'recipes/', RecipeListView.as_view()),
    path(r'register/', RegisterView.as_view()),
    path(r'login/', LoginView.as_view())
]
