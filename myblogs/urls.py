from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
]
