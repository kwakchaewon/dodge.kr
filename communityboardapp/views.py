from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from testapp.models import Boards


def goToMain(request):
    return render(request, 'main.html')

def goLogin(request):
    return render(request, 'login.html')