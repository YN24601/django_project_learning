from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

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

def news_view(request, topic: str):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except KeyError:
        result = "Page not found"
        # return HttpResponseNotFound(result)
        raise Http404(result)

def news_time_view(request, topic, year):
    return HttpResponse(articles[topic] + ' in the year ' + str(year))

# redirects
# domain.com/my_app/0 ---> domain.com/my_app/sports
# ...
def num_page_redirect_view(request, num: int):
    topic_list = list(articles.keys())
    topic = topic_list[num]
    # return HttpResponseRedirect(topic)
    return HttpResponseRedirect(reverse('news_topic', args=[topic, ]))
    


