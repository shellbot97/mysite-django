from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


def content_file_name(instance, filename):
    return '/'.join(['myblogs', instance.user.username, filename])


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    category_slug = models.CharField(max_length=200, default=1)
    is_active = models.BooleanField(default=True)
    added_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + ' - ' + self.category_slug


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)
    is_active = models.BooleanField(default=True)
    added_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    img = models.FileField(upload_to=content_file_name, blank=True, default='', null=True)
    sub_category = models.ForeignKey(SubCategory, default=1, on_delete=models.SET_DEFAULT)
    is_active = models.BooleanField(default=True)
    added_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title + ' - ' + self.description


class Comment(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    comment_title = models.CharField(max_length=250)
    comment_content = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    added_date = models.DateTimeField(default=datetime.now)
