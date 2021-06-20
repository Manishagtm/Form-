from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign/', views.sign, name='sign'),
    path('two/', views.two, name='two'),
    path('login/', views.login, name='login'),
    ]
