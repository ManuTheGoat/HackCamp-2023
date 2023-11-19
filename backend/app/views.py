#from argon2 import PasswordHasher
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from app.models import User, Entry, ListEntry

def signup(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    username: str = str(request.POST['username'])
    password: str = str(request.POST['password'])

    if len(username) < 5 or len(username) > 16:
        return HttpResponse(json.dumps({
            'error': 'Username must be between 5-16 characters'
        }), status=400, content_type='application/json')

    if not username.replace('_', '').isalnum():
        return HttpResponse(json.dumps({
            'error': 'Username can only contain alphanumerical characters and underscores (_)'
        }), status=400, content_type='application/json')

    if len(password) < 8:
        return HttpResponse(json.dumps({
            'error': 'Password must be at least 8 characters long'
        }), status=400, content_type='application/json')

    password_hash = PasswordHasher().hash(password)

    pass

def login(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    username: str = str(request.POST['username'])
    password: str = str(request.POST['password'])

    if len(username) < 5 or len(username) > 16:
        return HttpResponse(json.dumps({
            'error': 'invalid username'
        }), status=401, content_type='application/json')
    
    pass

def submit(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    location: str = str(request.POST['location'])
    subject: str = str(request.POST['subject'])

    entry = Entry(location=location, subject=subject)
    entry.save()

def edit(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    location: str = str(request.POST['location'])
    subject: str = str(request.POST['subject'])

    #

def list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    page_number = request.GET['page']

    entries = []

    list_entries = ListEntry.objects.all().order_by('id')[(page_number - 1) * 3:page_number * 3]
    for list_entry in list_entries:
        entry = Entry.objects.get(id=list_entry.entry)
        user = User.objects.get(id=entry.user)
        entries.append({
            'profile': '',
            'username': user.username,
            'subject': entry.subject,
            'location': entry.location
        })

    return HttpResponse(json.dumps(entries))

def chat(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    #

    pass

# chat

#study button
