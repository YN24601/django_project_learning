from django.urls import path
from . import views

# url=domain/app_name/view_name

'''
urlpatterns = [
    # /my_app/index_view/
    path('index_view/', views.index, name='index'),
    path('sports/', views.sports_view, name='sports'),
    path('music/', views.music_view, name='music')
]
'''
urlpatterns = [
    # path('<topic>/', views.news_view)
    path('<str:topic>/', views.news_view),
    path('<str:topic>/<int:year>/', views.news_time_view)
]

