import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from . import serializers
from .models import *

def check_token(token):
    try:
        return User.objects.get(token = token)
    except User.DoesNotExist:
        return None

def get_user(id):
    try:
        return User.objects.get(id = id)
    except User.DoesNotExist:
        return None

def do_login(username,passwd):
    try:
        return User.objects.get(username = username, passwd = passwd)
    except User.DoesNotExist:
        return None

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def add_user(request):
    if not check_token(request.data.get('token')):
        return Response({'error':'require correct token'},status = status.HTTP_400_BAD_REQUEST)

    serializer = serializers.UserSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def login(request):
    username = request.data.get('username')
    passwd = request.data.get('passwd')
    user = do_login(username, passwd);
    print(user)
    if user:
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def get_user_by_id(request,id):
    user = get_user(id)
    if user:
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_note(request):
    if not check_token(request.data.get('token')):
        return Response({'error':'require correct token'},status = status.HTTP_400_BAD_REQUEST)

    serializer = serializers.NoteSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_notes(request,username):
    notes = Note.objects.filter(username = username)
    if notes:
        serializer = serializers.NoteSerializer(notes, many = True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_type(request):
    if not check_token(request.data.get('token')):
        return Response({'error':'require correct token'},status = status.HTTP_400_BAD_REQUEST)

    serializer = serializers.TypeSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_types(request, username):
    types = Type.objects.filter(username = username)
    if types:
        serializer = serializers.TypeSerializer(types, many = True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(status = status.HTTP_404_NOT_FOUND)

