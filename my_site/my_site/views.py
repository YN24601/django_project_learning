from django.shortcuts import render

def my_custom_page_not_found_view(request, exception):
    # return render(request, 'my404.html')
    return render(request, '404.html')