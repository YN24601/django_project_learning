# Personal Learning Project

Personal learning project to explore bootstrap and Django.

- [Personal Learning Project](#personal-learning-project)
  - [Setup](#setup)
    - [1. Start a django project](#1-start-a-django-project)
    - [2. Create a django application(App)](#2-create-a-django-applicationapp)
  - [Views, Rounting, URL](#views-rounting-url)
    - [1. Connect a View to a URL with path()](#1-connect-a-view-to-a-url-with-path)
    - [2. Create a homepage view](#2-create-a-homepage-view)
    - [3. Dynamic routing](#3-dynamic-routing)
    - [4. 404 error handling](#4-404-error-handling)
    - [5. Redirect](#5-redirect)
      - [Redirect with reverse function](#redirect-with-reverse-function)
  - [Views \& Templates](#views--templates)
    - [1. Create templates and connect to views](#1-create-templates-and-connect-to-views)
    - [2. Template directory and rendering](#2-template-directory-and-rendering)
      - [start a new project:](#start-a-new-project)
  - [Django template language](#django-template-language)
    - [1. Template variable and context](#1-template-variable-and-context)
    - [2. Template Comment](#2-template-comment)
    - [3. Filters and Tags](#3-filters-and-tags)
    - [4. Tags and URL mapping](#4-tags-and-url-mapping)
    - [5. Template inheritance](#5-template-inheritance)
    - [5. Custom 404 Templates](#5-custom-404-templates)
    - [6.](#6)

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

ep: > python3 manage.py startapp blog

which creates the following structure:

- app_name
  - \_\_init__.py -->>> package init file
  - admin.py -->>> admin interface for the app
  - apps.py -->>> app config
  - models.py
  - tests.py
  - views.py
  - migrations -->>> database migrations
    - \_\_init__.py -->>> package init file
- db.sqlite3 -->>> database file

No urls.py file is created in the app folder, but it's created in the project folder. So we need to mannualy create urls.py files for each app.
Then link the app urls.py file to the project urls.py file using the include() function from django.urls module, to rout views.py files through urls.py files, which is called routing.

## Views, Rounting, URL

how views connect to urls before passing informatin to templates.

### 1. Connect a View to a URL with path()

- route
- view

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
#----------------
urlpatterns = [
    path('<str:topic>/', views.news_view),
]
```

with multiple parameters

```python
def news_time_view(request, topic, year):
    return HttpResponse(articles[topic] + ' in the year ' + str(year))
#----------------
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

## Django template language

### 1. Template variable and context

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

### 2. Template Comment

syntax:

```html
{# comment #}
```

or

```html
{% comment %}
comment
{% endcomment %}
```

### 3. Filters and Tags

A filter is a function that is applied to a variable before it is displayed in the template. That's very similar to the filter function in python. Syntax: {{ variable_name | filter_name }}

```html
    {{ key1 | upper }}
    {{ key1 | length}}
    {{ key1 | lower | capfirst}}
```

Django can provied further logic in the template by using tags that are embedded in the template language. Synax:

```html
{% tag_name %}
{{ variable_name }}
{% endtag_name %}
```

eg: for-loop

```html
<ul>
    {% for item in listkey %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

There are a lot of built-in tags and filters in Django, see the [official documentation](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/). When using tags, it's important to mind the spacing, otherwise it may cause syntax error.

### 4. Tags and URL mapping

Tag `url` can be used to map the url to the view function, instead set the path in the href attribute in the html file.

1. in the urls.py file, define the `app_name` and the `name` parameter in the path function

    ```python
    app_name = 'my_app'
    urlpatterns = [
        path('', views.example_view, name='example'),
        path('variable/', views.variable_view, name='variable'),
    ]
    ```

2. Use the `url` tag in the template file

    ```html
    <a href="{% url "my_app:variable" %}">go to variable page</a>
    ```

    if the template file is in the site level folder, the url tag should be `{% url "variable" %}`, but changes are needed when the template file is in the site level folder, see next section.

### 5. Template inheritance

Use the `block` tag to define the block in the base template file, and use the `{% extends "base.html" %}` tag to inherit the template file. Usually used when the template file is shared by multiple views, such as the header and footer of the website.

In the base template file, define the block by using the `{% block block_name %}` tag.

```html
{% block block_name %}
block content
{% endblock %}
```

In the child template file, use the `{% extends "base.html" %}` tag to inherit the base template file, and use the `{% block block_name %}` tag to override the content of the block.

```html
{% extends "base.html" %}

{% block content %}
child content
{% endblock %}

```

to extend the base.html file in the project level folder, the 'DIRS' parameter in the TEMPLATES setting should be set to the folder.

```python
import os
#--------

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    }]
```

See [base.html](my_site/templates/base.html) and [child.html](my_site/my_app/templates/my_app/child.html) for more details.

### 5. Custom 404 Templates

There are built-in 404 templates in Django, but it's not easy to customize them. To customize the 404 template, create a new file named `404.html` in the sit level `templates` folder. Change DEBUG to False, and set ALLOWED_HOSTS to the host name of the website, Django will automatically use this file as the 404 template.

To customized different types of error pages, create different files named `404.html`, `403.html`, `400.html`.

The error page can also be renamed to spicific customized name, such as `my404.html` et al. This need to be rendered in the views.py file created in the site level folder, and use handler404 parameter to specify the error view in url.py file. See [views.py](my_site/my_site/views.py) [url.py](my_site/my_site/urls.py) for more details.

> Note: when creating the error view function, there should have an exception parameter.

But it's not recommended to rename the error page, because it's not friendly to co-wokers. Just keep the default 404 page name, and the render procedure stated above will work.

### 6.