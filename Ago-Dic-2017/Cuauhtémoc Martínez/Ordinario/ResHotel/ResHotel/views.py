from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'base/index.html')

def ee(request):
    return render(request, 'base/ee.html')
