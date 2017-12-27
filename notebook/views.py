import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from . import serializers
from . import database
from .models import PageView
from .models import User

def index(request):
    return render(request, 'notebook/index.html')

def health(request):
    return HttpResponse(PageView.objects.count())

def editor(request):
    return render(request, 'notebook/editor.html')

def register(request):
    return render(request, 'user/register.html')
