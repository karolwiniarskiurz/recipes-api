from django.urls import path, include
from rest_framework import routers

from api.views.login_view import LoginView
from api.views.user_view import UserViewSet
from api.views.group_view import GroupViewSet
from api.views.recipe_detail_view import RecipeDetailView
from api.views.recipe_list_view import RecipeListView
from api.views.register_view import RegisterView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('recipes/<int:id>/', RecipeDetailView.as_view()),
    path(r'recipes/', RecipeListView.as_view()),
    path(r'register/', RegisterView.as_view()),
    path(r'login/', LoginView.as_view()),
]
