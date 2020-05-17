from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    # path('', views.login_user, name='login_user'),  # default url (this will take user to the login page)
    # path('logout', views.logout_user, name='logout_user'),
    # path('register', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
