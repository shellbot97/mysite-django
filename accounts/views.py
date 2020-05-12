from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login')
def profile(request):
    return render(request, 'profile.html', {"user": request.user})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('accounts:profile')
            else:
                return HttpResponse("account disabled")
        else:
            return HttpResponse("invalid cred")
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')
