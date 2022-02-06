from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from testapp.models import Boards


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

# def goRegistUser(request):
#  # return redirect('accounts:login')