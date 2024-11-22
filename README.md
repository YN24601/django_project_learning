# Personal Learning Project

Personal learning project to explore bootstrap and Django.

## Setup

### 1. Start a django project

run the following command in the terminal:
> django-admin startproject project_name
which creats the following structure:
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

ep: python3 manage.py startapp blog

which creats the following structure:
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


