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

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

def get_user(id):
    try:
        return User.objects.get(id = id)
    except User.DoesNotExist:
        return Http404

@api_view(['POST'])
def add_user(request):
    serializer = serializers.UserSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_user_by_id(request,id):
    user = get_user(id)
    serializer = serializers.UserSerializer(user)
    return Response(serializer.data)
