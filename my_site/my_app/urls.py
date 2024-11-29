from django.urls import path
from . import views

urlpatterns = [
    path('', views.example_view, name='index'),
    path('variable/', views.variable_view, name='variable'),
]