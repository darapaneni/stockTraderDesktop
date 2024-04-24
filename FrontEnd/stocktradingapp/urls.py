from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portifolio/', views.portifolio, name='portifolio'),
    path('buy/', views.buy, name='buy'),
    path('purchased/', views.purchased, name='purchased'),
]

