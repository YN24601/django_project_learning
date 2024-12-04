from django.urls import path
from . import views

# domain.com/office/
urlpatterns = [
    path('patients/', views.list_patients, name='list_patients'),
]