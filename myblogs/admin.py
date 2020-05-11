from django.contrib import admin
from .models import Category, SubCategory, Blog, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Blog)
admin.site.register(Comment)