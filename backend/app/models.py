from django.db import models

class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=200)

class Entry(models.Model):
    location = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
