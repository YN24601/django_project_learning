# Personal Learning Project

Personal learning project to explore bootstrap and Django.

## Setup

### 1. Start a django project

run the following command in the terminal:
> django-admin startproject project_name
which creates the following structure:
* project_name
    * \_\_init__.py -->>> package init file
    * settings.py -->>> config setting for the project
    * urls.py -->>> url routing for the project
    * asgi.py -->>> ASGI config for the project; web server gateway interface
    * wsgi.py -->>> WSGI config for the project; web server gateway interface
* manage.py -->>> command line utility for administrative tasks

get into this folder and run the following command in the terminal:

> python3 manage.py runserver 

to run the server on a designated port 
> python3 manage.py runserver 8080

ctrl + c to stop the server

### 2. Create a django application(App)

When refering to __application__ of a Django project, it's not a website app, but a module of the website for a specific functionality.

run the following command in the terminal:
> python3 manage.py startapp app_name

ep: 
> python3 manage.py startapp blog

which creates the following structure:
* app_name
    * \_\_init__.py -->>> package init file
    * admin.py -->>> admin interface for the app
    * apps.py -->>> app config
    * models.py
    * tests.py
    * views.py
    * migrations -->>> database migrations
        * \_\_init__.py -->>> package init file
* db.sqlite3 -->>> database file

No urls.py file is created in the app folder, but it's created in the project folder. So we need to mannualy create urls.py files for each app.
Then link the app urls.py file to the project urls.py file using the include() function from django.urls module, to rout views.py files through urls.py files, which is called routing.

## Views, Rounting, URL
how views connect to urls before passing informatin to templates.

__Function based views__
### 1. Connect a View to a URL with path():
* route
* view

```python
 urlpatterns = [
    path('my_app/', include('my_app.urls')),
    path('admin/', admin.site.urls),
 ]
```

url=domain/app_name/view_name
### 2. Create a homepage view 
```python
def home_view(request):
    return HttpResponse("Home page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view)
]
```

it can also be done by creating a views.py file in the site folder and connecting the view to the url in the urls.py file.

### 3. Dynamic routing

use a dictionary to store different pages and pass the key as a parameter to the view function.

```python
articles = {
    'sports': 'Sports Page',
    'music': 'Music Page',
    'finance': 'Finance Page',
}

def news_view(request, topic):
    return HttpResponse(articles[topic])
###########
urlpatterns = [
    path('<str:topic>/', views.news_view),
]
```

with multiple parameters

```python
def news_time_view(request, topic, year):
    return HttpResponse(articles[topic] + ' in the year ' + str(year))
###########
urlpatterns = [
    path('<str:topic>/<int:year>/', views.news_time_view)
]
```

### 4. 404 error handling

use try except to handle errors and raise Http404 to display error message or redirect to another page.

```python
def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except KeyError:
        result = "Page not found"
        # return HttpResponseNotFound(result)
        raise Http404(result) # or redirect to a 404.html page
```
When using HttpResponseNotFound, there will be a 404 error message, but when using raise Http404, the error message will be displayed in the browser. That's because the raise function will start the error handling process(debug mode). To display the error message in the browser, we need to change the DEBUG = True in the settings.py file to DEBUG = False, and set the ALLOWED_HOSTS = ["127.0.0.1"] to allow the browser to access the website.

The debug mode is only used for development, and should be turned off when deploying the website to production.

```python
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]
```

### 5. Redirect

use HttpResponseRedirect to redirect to another page. Add a redirect function to the views.py file, and add a url to the urls.py file.

```python
### views.py
# domain.com/my_app/0 ---> domain.com/my_app/sports
# domain.com/my_app/1 ---> domain.com/my_app/music
# ...
def num_page_redirect_view(request, num):
    topic_list = list(articles.keys())
    topic = topic_list[num]
    return HttpResponseRedirect(topic)

### urls.py
urlpatterns = [
    path('<int:num>/', views.num_page_redirect_view), 
    # ...
]
```

#### Redirect with reverse function

An error occure when I'm using relative url in the HttpResponseRedirect function. So when visiting domain.com/my_app/0, it will append the url to the current url, so the url will be redirect to domain.com/my_app/0/sports instead of domain.com/my_app/sports.
To fix this problem, I need to use absolute url by reference the url name.

First, I need to set the routing name for the news_view function in the urls.py file.
```python
urlpatterns = [
    path('<int:num>/', views.num_page_redirect_view), 
    path('<str:topic>/', views.news_view, name='news_topic'),
    path('<str:topic>/<int:year>/', views.news_time_view)
]
```

Then, import reverse function from django.urls, and get the absolute url in HttpResponseRedirect function.

```python
from django.urls import reverse
def num_page_redirect_view(request, num):
    topic_list = list(articles.keys())
    topic = topic_list[num]
    return HttpResponseRedirect(reverse('news_view', args=(topic,)))
```

The above can also done without reverse function by manually setting the url. But using reverse function is more convenient and less error-prone.


## Views & Templates

the relationship between views and templates.

### 1. Create templates and connect to views

create a templates folder in the app folder and create html files in the templates folder. And add the folder path to the TEMPLATES in the settings.py file, by using os.path.join function to connect the BASE_DIR and the templates folder.

```python
# settings.py
import os
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]
```
```python  
# views.py
from django.shortcuts import render
def simple_view(request):
    return render(request, 'my_app/example.html')
```
```python
# my_app/urls.py
urlpatterns = [
    path('', views.simple_view), # domain.com/my_app/
]
```

### 2. Template directory and rendering

Usually the template foders are separated base on their applictions, the foder name is the same as the app name. So we need to register the custom appliction ,and its cooresponding template folder in the settings.py file. [vedio link]( https://www.bilibili.com/video/BV16a41147Xh/?p=58)

#### start a new project:

Create a new project and add a application by using the command:
> django-admin startproject my_site             
> cd my_site                       
> python3 manage.py startapp my_app

Then create urls.py in the my_app folder, to connect the views and site-urls. 
Add function in the views.py file, and render the template in the function.

run the command: (this will be really useful when using the models)
> python3 manage.py migrate

add the appliction configuration class from apps.py file in the settings.py file.
```python
INSTALLED_APPS = [
    'my_app.apps.MyAppConfig',
]
```

run the command: 
> python3 manage.py makemigrations my_app

Now the project will not need to worry about the DIRS of templates in the setting.py, because the templates folder will be in the my_app folder (APP_DIR should be set to True in the settings.py file).

Create a template folder in the my_app folder, and create html files in the folder, which should be the same as the rendered html file name in views.py

run the project by using the command:
> python3 manage.py runserver

#### Template variable and context

The context is a dictionary that contains the data that will be passed to the template when using the render function.

```python
def variable_view(request):
    my_var = {'key': 'value'}
    return render(request, 'my_app/variable.html', context=my_var)
```

The dictionary values can be accessed in the template by using the {{ variable_name.key }} syntax.

```html
<body>
        {{ key1 }}
        {{ listkey.0 }}
</body>
```

#### Template comment

```html
{# comment #}
```

#### Template inheritance

The template inheritance is a way to share the common code between the templates. The base template is the template that contains the common code, and the child template is the template that inherits the base template.

### 3. Django template language



### 4. Template specific context

### 5. Exercise
