from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    # path('', views.register, name='register'),
    path('profile', views.profile, name='profile'),
]
