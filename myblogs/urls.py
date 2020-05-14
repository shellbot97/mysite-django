from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.create_blog, name='add-blog'),
    path('bulk_add', views.bulk_create_blog, name='bulk-add-blog'),
    path('<blog_id>', views.detail, name='blog-detail'),
    path('update/<blog_id>', views.update, name='blog-update'),
    path('delete/<blog_id>', views.delete, name='blog-delete'), # TODO add search album functionality, add bulk upload albums functionality
]
