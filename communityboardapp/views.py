from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from testapp.models import Boards
import logging
from django.contrib.auth.models import User
from django.contrib import auth

def goToMain(request):
    return render(request, 'main.html')

def goLogin(request):
    return render(request, 'login.html')

def goSignIn(request):
    return render(request, 'login.html')

def goSignUp(request):
    return render(request, 'signup.html')

def goCommunity(request):
    return render(request, 'community.html')

def signupCompleted(request):

    if request.method == "POST":
        username = request.POST['container__id']
        password = request.POST['container__pw']
        email = request.POST['container__email']
        phone = request.POST['container__phonenum']

        # last_name = request.POST['container__name']
        # birth = request.POST['container__birth']
        # userName = request.POST['container__id']

        user = User.objects.create_user(username, password, email)
        print("3")
        return redirect('/')
    print("4")
    return render(request, 'errorpage.html')

# def goRegistUser(request):
#  # return redirect('accounts:login')