from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.line_chart, name='line_chart'),
]
