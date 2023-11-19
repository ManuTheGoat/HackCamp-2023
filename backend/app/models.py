from django.db import models

class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=200) # TODO: find the length of a bcrypt hash
