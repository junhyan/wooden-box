from django.db import models

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = StringField(max_length=50)
    email = StringField(max_length=50)
    mobile = StringField(max_length=50)
    passwd = StringField(max_length=50)
