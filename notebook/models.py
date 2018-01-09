from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import uuid

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    passwd = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=100, default = make_password(uuid.uuid1(), None, 'pbkdf2_sha256'))

class Note(models.Model):
    topic = models.CharField(max_length=50, null=True)
    time = models.CharField(max_length=50, null=True)
    author = models.CharField(max_length=50, null=True)
    content = models.TextField()
    note_type = models.CharField(max_length=32, null=True)
    username = models.CharField(max_length=50, default='root')


class Type(models.Model):
    note_type = models.CharField(max_length=32)
    username = models.CharField(max_length=50, default='root')

