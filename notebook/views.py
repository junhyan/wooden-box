import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


from . import database
from .models import PageView

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

def health(request):
    return HttpResponse(PageView.objects.count())
