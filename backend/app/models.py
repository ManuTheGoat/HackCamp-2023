from django.db import models
import uuid

class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=200)
    entry = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    conversations = models.JSONField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Entry(models.Model):
    location = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    user = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class ListEntry(models.Model):
    entry = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    id = models.DateTimeField(auto_now_add=True, primary_key=True)

class Conversation(models.Model):
    users = models.JSONField()
    messages = models.JSONField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Message(models.Model):
    message = models.TextField(max_length=1000)
    user = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    conversation = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
