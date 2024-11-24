from django.shortcuts import render
from django.http import HttpResponse

articles = {
    'sports': 'Sports Page',
    'music': 'Music Page',
    'finance': 'Finance Page',
}

# Create your views here.
def index(request):
    return HttpResponse("Hello. This is a view inside MY_APP")

'''
def sports_view(request):
    return HttpResponse("This is a sports view")

def music_view(request):
    return HttpResponse("This is a music view")
'''

def news_view(request, topic):
    return HttpResponse(articles[topic])

def news_time_view(request, topic, year):
    return HttpResponse(articles[topic] + ' in the year ' + str(year))

