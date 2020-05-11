from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog


# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return HttpResponse(blogs)
