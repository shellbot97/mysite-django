import requests
from django.conf import settings
from django.shortcuts import render, redirect


class AuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # print(request)
        # if not request.user.is_authenticated:
        #     return redirect('accounts:login_user')
        # Code to be executed for each request/response after
        # the view is called.
        return response
