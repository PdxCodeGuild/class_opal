# Launching

------------------------------------------------------

### Setup

[ ] Create new git branch

[ ] Create and acivate (or activate existing) virtualenv

[ ] `pip install django`

------------------------------------------------------
### Start Project

```bash
django-admin startproject [PROJECTNAME]
cd [PROJECTNAME]
python manage.py startapp [APPNAME]
```

------------------------------------------------------
### Create View

in [APPNAME]/views.py:  

```python
from django.http import HttpResponse

def index(request):  
    return HttpResponse("Hello, world")  
```

------------------------------------------------------

### Create Route

Create a new `urls.py` file in your app folder

```python
from django.urls import path

from . import views

app_name = '[APP_NAME]'
urlpatterns = [
    path('', views.index, name='index'),
]
```

in `[PROJECTNAME]/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path <-- add "include"

urlpatterns = [
    path('[APP ]/', include('[APPNAME].urls')),
    path('admin/', admin.site.urls),
]
```
NOTE: your route does NOT have to share the name of your app (but it probably should)

------------------------------------------------------

### Create Templates

All HTML files should be added to `[APP_NAME]/templates/[APP_NAME]/`


------------------------------------------------------
### Create Models

Add your models to `models.py` in your app folder

------------------------------------------------------
### Migrate Models


in `[PROJECTNAME]/settings.py`:

```python
INSTALLED_APPS = [
    '[APPNAME].apps.[Appname]Config',
    ...
]
```
Note: This is the path to a class that Django wrote for you! You can find it in `apps.py` in your app folder


```bash
py manage.py makemigrations [APPNAME]
py manage.py migrate 
```
------------------------------------------------------

### Use the Admin Site

```bash
python manage.py createsuperuser
```


in `admin.py` in your app folder:

```python
from django.contrib import admin

from .models import ModelName

admin.site.register(ModelName)
```

then navigate to `http://localhost:8000/admin` in your browser and log in


