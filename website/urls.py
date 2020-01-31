from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('recipe/<int:id>/', views.detail, name='detail'),
    path('404/', views.notfound, name='notfound')
]
