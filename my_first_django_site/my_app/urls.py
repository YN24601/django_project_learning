from django.urls import path
from . import views

# url=domain/app_name/view_name

urlpatterns = [
    # /my_app/index_view/
    path('index_view/', views.index, name='index')
]