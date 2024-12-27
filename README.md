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
      - [start a new project](#start-a-new-project)
  - [Django template language](#django-template-language)
    - [1. Template variable and context](#1-template-variable-and-context)
    - [2. Template Comment](#2-template-comment)
    - [3. Filters and Tags](#3-filters-and-tags)
    - [4. Tags and URL mapping](#4-tags-and-url-mapping)
    - [5. Template inheritance](#5-template-inheritance)
    - [5. Custom 404 Templates](#5-custom-404-templates)
    - [6. Static Files with Tags](#6-static-files-with-tags)
  - [Model and Database](#model-and-database)
    - [1. Migration and creating a Model](#1-migration-and-creating-a-model)
    - [2. Data Iteration](#2-data-iteration)
      - [1. Create](#1-create)
      - [2. Reading and Querying](#2-reading-and-querying)
      - [3. Updating](#3-updating)
        - [1. Update models](#1-update-models)
        - [2. Update database entries](#2-update-database-entries)
      - [4. Deleting](#4-deleting)
    - [3. Connecting templates and Database models](#3-connecting-templates-and-database-models)
  - [Django Admin](#django-admin)
    - [1. Create a new site](#1-create-a-new-site)
    - [1. Create a superuser](#1-create-a-superuser)
    - [2. Connecting models to admin](#2-connecting-models-to-admin)
    - [3. Customizing the admin interface](#3-customizing-the-admin-interface)
  - [Django Forms](#django-forms)
    - [1. Get, Post and CSRF](#1-get-post-and-csrf)
    - [2. Django Form Class Basics](#2-django-form-class-basics)
    - [4. Form Widgets and CSS styling](#4-form-widgets-and-css-styling)
    - [5. Model Forms](#5-model-forms)
  - [Class-based Views](#class-based-views)
  - [Django Deployment](#django-deployment)

## Setup

### 1. Start a django project

run the following command in the terminal:
> django-admin startproject project_name
which creates the following structure:

- project_name
  - \_\_init__.py -->>> package init file
  - settings.py -->>> config setting for the project
  - urls.py -->>> url routing for the project
  - asgi.py -->>> ASGI config for the project; web server gateway interface
  - wsgi.py -->>> WSGI config for the project; web server gateway interface
- manage.py -->>> command line utility for administrative tasks

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

#### start a new project

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

### 6. Static Files with Tags

Django provides a built-in static files management system, which can be used to manage static files such as CSS, JavaScript, images, etc. in the project. Instead of having to refer them by paths, Django provides a way to refer to them by using Tags.

It's similar to the [{% url %}](#4-tags-and-url-mapping) tag, but using {% static %} tag.

1. check if 'django.contrib.staticfiles' is in INSTALLED_APPS. It is already in the default settings.py file, so no need to add it manually, just make sure it's not commented out. \
2. make sure the 'STATIC_URL' is set to '/static/'. This path is the path that Django will use to refer to static files, it can be changed to any path, but it's recommended to use '/static/'.
3. create a static folder in the app level folder, and a subdirectory named the same as the app name (same as the templates folder). This is the folder that Django will use to store static files for the app.
4. Move the static files to the static folder.
5. Call {% load static %} in the template file.'

    ```html
    {% extends "base.html" %}
    {% load static %}

    {% block content %}
        <img src="{% static 'my_app/IMG.jpg' %}" alt="my image" width="200" height="200">
    {% endblock content %}
    ```

## Model and Database

In this section, the focus is on how to use Django's ORM to interact with the database (CRUD-Create, Read, Update, Delete). The database used is SQLite, which is already included in Django.

### 1. Migration and creating a Model

Django Models are defined in the models.py file in the app level folder. Its a class that converts python codes to SQL commands.

Migration is the process of applying the changes made to the model to the database. It's a set of instructions that will be used to apply the changes to the database. There are three commands that can be used to manage migrations:

- makemigretions: create the set of instructions that will be used to apply the changes to the database.
    > python manage.py makemigrations [app_name]
    a migration file will be created in the app level folder.
- migrate: run existing migrations created by makemigrations to apply the changes to the database.
    > python manage.py migrate
- sqlmigrate: show the SQL commands that will be executed by the migration.
    > python manage.py sqlmigrate [app_name] [migration_code]

Steps to create a model and migrate it to the database:

1. Start a new project.
2. Initial project migrate command: `python manage.py migrate` to create the database. It will automatically create tables accroding to the models defined in the app.
3. Create an app and a model.
4. Register the app class in the INSTALLED_APPS list in settings.py `'office.apps.OfficeConfig'`
5. Run `python manage.py makemigrations [app_name]` for the app to create the [migration file](my_site_01/office/migrations/0001_initial.py).
6. Run `python manage.py migrate` for new migrations to apply the changes to the database.

### 2. Data Iteration

use command `python3 manage.py shell` to interact with the project in the shell.

#### 1. Create

3 methods to create new data entries:

- Instance an object and object_name.save()

    ```python
    patient = Patient(first_name='cark', last_name='smith', age=30)
    patient.save()
    ```

- Class_name.object.create()

    ```python
    Patient.objects.create(first_name='susan', last_name='smith', age=28)
    ```

- Class_name.object.bulk_create()

    ```python
    mylist = [
        Patient(first_name='yana', last_name='zhang', age=23), 
        Patient(first_name='adam', last_name='smith', age=60)
        ]
    Patient.objects.bulk_create(mylist)
    ```

#### 2. Reading and Querying

methods to query data: .all(), .get(), .filter(), .exclude() and using operators.

- .all() returns all the objects in the database.

    ```python
    Patient.objects.all()
    ```

- .get() returns a single object that matches the given parameters.

    ```python
    Patient.objects.get(first_name='cark')
    Patient.objects.get(first_name='cark', last_name='smith')
    Patient.objects.get(pk=1) # get the object with primary key(pk)
    ```

- .filter() returns a QuerySet of objects that match the given parameters.

    ```python
    Patient.objects.filter(last_name='smith')
    Patient.objects.filter(last_name='smith').filter(age=30)
    ```

- .exclude() returns a QuerySet of objects that do not match the given parameters.

    ```python
    Patient.objects.exclude(last_name='smith')
    ```

- using Q() to specify complex queries, '__' to specify the field. See details in [Django documentation](https://docs.djangoproject.com/en/5.1/topics/db/queries/#complex-lookups-with-q-objects).
  
    ```python
    from Django.db.models import Q
    Patient.objects.filter(Q(first_name='cark') | Q(last_name='smith'))
    Patient.objects.filter(Q(first_name='cark') & Q(last_name='smith'))
    Patient.objects.filter(~Q(first_name='cark'))
    Patient.objects.filter(last_name__startswith='s')
    Patient.objects.filter(age__gt=30)
    ```

#### 3. Updating

##### 1. Update models

When add new attributes to the models, need to define a default value for them. Use validator to check the if the data is resonable.

```py
from django.core.validators import MinValueValidator, MaxValueValidator

    heartrate = models.IntegerField(default=60, validators=[MinValueValidator(0), MaxValueValidator(200)])
```

After adding new attributes, remember to migrate the database.

> python manage.py makemigrations
> python manage.py migrate

##### 2. Update database entries

- update the object attributes, then use save() method to update the database.

    ```python
    yana = Patient.objects.get(first_name='yana')
    yana.heartrate = 65
    yana.save()
    ```

#### 4. Deleting

- delete() method to delete the objects.

    ```python
    yana=Patient.objects.filter(first_name='yana')
    yana.delete()
    ```

### 3. Connecting templates and Database models

Create a view function in [views.py](my_site_01/office/views.py), import the model and use it in the view function, then render the template.

In [templates](my_site_01/office/templates/office/list.html), use django template language to display the data.

In [urls.py](my_site_01/office/urls.py), import the view function and add it to the url pattern, connect the url path to the [site url.py](my_site_01/my_site_01/urls.py).

## Django Admin

Django admin is a built-in application that allows you to manage your database through a web interface.

### 1. Create a new site

Create [my_car_site](my_car_site):
> django-admin startproject my_car_site
> cd my_car_site
> python3 manage.py startapp cars

- Create project level templates folder and add [base.html](my_car_site/templates/base.html) to it, using os.path.join(BASE_DIR, 'templates').

- Create app level templates folder and add html files to it. Add the path to the [settings.py](my_car_site/my_car_site/settings.py)
- Connect the templates to the views in [views.py](my_car_site/cars/views.py).
- Create an [urls.py](my_car_site/cars/urls.py) in the app folder, set app_name for namespacin, and add the url patterns.
- Include the app urls in the project level [urls.py](my_car_site/my_car_site/urls.py).
- Add the AppConfig class in [app.py](my_car_site/cars/apps.py) and add the app to the installed apps in [settings.py](my_car_site/my_car_site/settings.py).

- Create a car model in the [cars/models.py](my_car_site/cars/models.py) file.
- Add functionality to the views.py file.
- Create HTML forms to send data to the views.

> python3 manage.py makemigrations cars
> python3 manage.py migrate
> python3 manage.py runserver

### 1. Create a superuser

run the command:
> python3 manage.py createsuperuser

Set the username, email and pw.

Then run the server, and visit domain.com/admin/

### 2. Connecting models to admin

To connect the models to Django Admin interface, we need to import the model inside the [admin.py](my_car_site/cars/admin.py) file and register it.

'''python
from .models import Cars
admin.site.register(Car)
'''

Run the server, and there will be a Cars administration page. Superuser can add, edit, delete and view the cars data.

site: domain.com/admin/application_name/model_name/instance_id/

### 3. Customizing the admin interface

To customize the admin interface, we need to define a ModelAdmin calss in the [admin.py](my_car_site/cars/admin.py) file. See [website](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#modeladmin-objects) for more details.

## Django Forms

Traditional HTML forms are used to send data to the server, which requires a lot of processing to connect with Django, see [1. Create a new site](#1-create-a-new-site). Django have this build-in Forms class to make it easier to send data to the server through using the Tag `{{forms}}`

### 1. Get, Post and CSRF

- Get: request data from the server, and display it on the page.
- Post: send data to the server.
- CSRF: Cross Site Request Forgery, a security feature to prevent the data from being sent to the server by a malicious website.

Gjango automatically add CSRF token to the form, and check it when the form is submitted. Just include the `{% csrf_token %}` in the form.

### 2. Django Form Class Basics

- Create a new [Django project](my_site_05) and add a new app(cars). Set up the app, templates, and connect the urls.

- Create a [forms.py](my_site_05/cars/forms.py) file in the app folder, and define a form class in it. By defining contributes, Django will automatically generate the HTML form fields and validation. See [website](https://docs.djangoproject.com/en/4.2/topics/forms/)for more details.

  ```python
    from django import forms

    class ReviewForm(forms.Form):
        first_name = forms.CharField(label='First Name', max_length=100)
        last_name = forms.CharField(label='Last Name', max_length=100)
        email = forms.EmailField(label='Email')
        review = forms.CharField(label='Write you review here', widget=forms.Textarea)
    ```

- Import the form class in the [views.py](my_site_05/cars/views.py) file, and pass it to the context.

    ```python
    from django.shortcuts import render, redirect
    from .forms import ReviewForm
    from django.urls import reverse

    # Create your views here.
    def rental_review(request):
        # Post Request  --> Form Content -->Thank you
        if request.method == 'POST':
            form = ReviewForm(request.POST)

            if form.is_valid():
                print(form.cleaned_data)
                return redirect(reverse('cars:thank_you'))
        # Else render the form
        else:
            form = ReviewForm()
        return render(request, 'cars/rental_review.html', context={'form':form})

    def thank_you(request):
        return render(request, 'cars/thank_you.html')
    ```

- Add Djange forms in the [rental_review.html](my_site_05/cars/templates/cars/rental_review.html) file. Use `form.as_p` to render the form fields.
  
    ```html
    <form action="POST">
        {% csrf_token %}
        {{form.as_p }}
        <input type="submit" value="Submit">
    </form>
    ```

### 3. Django Form Rendering

Django form can be rendered in different ways, see [website](https://docs.djangoproject.com/en/4.2/topics/forms/#rendering-forms) for more details.

- `form.as_p`: Render the form fields as a paragraph.

- `form.as_ul`: Render the form fields as a unordered list.

To access the form fields, we can use the `{{form.field_name}}` in the template.

- `form.field_name.lable_tag`: Render the label of the field.

A form field can also be looped.

```html
    <div class='container'>
    <form method="POST">
        {% csrf_token %}
        {% for field in form%}
        <div class='mb-3'>
            {{field.label_tag}} 
        </div>
        {{field}}
        {% endfor %}
        <input type="submit" value="Submit">
    </form>
```

### 4. Form Widgets and CSS styling

Form.py can render the actual HTML form tags, and the widget attributes can be customized to change the appearance of the form fields.

To begin with, create a [custom.css](my_site_05/cars/static/cars/custom.css) file in the static folder of the app, and add some CSS styles.

Then load the static files in the [rental_review.html](my_site_05/cars/templates/cars/rental_review.html) file by adding the following line at the top of the file.

```html
    {% load static %}
```

and then add the following line in the head section of the file.

```html
    <link rel="stylesheet" href="{% static 'cars/custom.css' %}">
```

Run the following command to register the static files.

```bash
    python manage.py 
```

Each form field can be customized by adding the `widget` attribute in the form class.

Core field attributes: see [website](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#core-field-arguments) for more details. Ep:

```python
    review = forms.CharField(label='Write you review here', widget=forms.Textarea)
```

How to style it? add attributes to the widget.

```python
    review = forms.CharField(label='Write you review here', widget=forms.Textarea(attrs={'class':'myform'}))
```


### 5. Model Forms

## Class-based Views

(80 min)

## Django Deployment

(40 min)
