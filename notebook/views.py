import os
from django.shortcuts import render
from django.http import HttpResponse

from .models import PageView

def index(request):
    return render(request, 'notebook/index.html')

def health(request):
    return HttpResponse(PageView.objects.count())

def editor(request):
    return render(request, 'notebook/editor.html')

def register(request):
    return render(request, 'user/register.html')
