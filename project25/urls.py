"""
URL configuration for project25 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form_html/',form_html,name='form_html'),
    path('form_wh/',form_wh,name='form_wh'),
    path('form_accessrec/',form_accessrec,name='form_accessrec'),
    path('select_multiple_webpage/',select_multiple_webpage,name='select_multiple_webpage'),
    path('checkbox/',checkbox,name='checkbox'),
    path('select_multiple_accessrecord/',select_multiple_accessrecord,name='select_multiple_accessrecord'),
    path('check_box/',check_box,name='check_box'),
]
