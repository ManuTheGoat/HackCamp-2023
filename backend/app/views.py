#from argon2 import PasswordHasher
import json
import uuid
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from app.models import User, Entry, ListEntry, Conversation, Message

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
    user_id = uuid.UUID(request.post['uuid'])

    entry = Entry.objects.get(id=User.objects.get(id=user_id).entry)
    entry.location = location
    entry.subject = subject
    entry.save()

    return HttpResponse(json.dumps({ 'success': True }), status=200, content_type='application/json')

def list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    page_number = int(request.GET['page'])

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

    return HttpResponse(json.dumps(entries), content_type='application/json')

def get_conversations(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    user_uuid = uuid.UUID(request.POST['uuid'])
    user = User.objects.get(id=user_uuid)
    conversations = user.conversations[len(user.conversations) - 10: len(user.conversations)]

    conversation_names = []
    for conversation in conversations:
        index = 0
        if conversation.users[0] == user_uuid:
            index = 1
        username = User.objects.get(id=conversation.users[index]).username
        conversation_names.append(username)

    return HttpResponse(json.dumps(conversation_names), content_type='application/json')

# starts a conversation
def study(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    user_uuid = uuid.UUID(request.post['uuid'])
    chosen_user_uuid = uuid.UUID(request.post['chosen_uuid'])

    conversation = Conversation(users=[user_uuid, chosen_user_uuid])

    user = User.objects.get(id=user_uuid)
    chosen_user = User.objects.get(id=chosen_user_uuid)

    user.conversations = user.conversations.append(conversation.id)
    user.save()
    chosen_user.conversations = chosen_user.conversations.append(conversation.id)
    chosen_user.save()

def chat(request): # sends a chat message
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    conversation_uuid = uuid.UUID(request.post['conversation_uuid'])
    message = request.post['message']

    conversation = Conversation.objects.get(id=conversation_uuid)
    conversation.messages = conversation.messages.append(message)
    conversation.save()

def get_messages(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    conversation_uuid = uuid.UUID(request.POST['conversation_uuid'])
    conversation = Conversation.objects.get(id=conversation_uuid)

    message_uuids = conversation.messages[len(conversation.messages) - 20: len(conversation.messages)]

    messages = []
    for message_uuid in message_uuids:
        message = Message.objects.get(id=message_uuid)
        author = User.objects.get(id=message.user)
        messages.append({
            'message': message.message,
            'user': author.username
        })
    
    return HttpResponse(json.dumps(messages), content_type='application/json')
