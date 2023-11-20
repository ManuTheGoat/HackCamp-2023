from django.test import TestCase
from app.models import User, Entry, ListEntry, Conversation, Message
import time

user1 = User(username="1", password="test")
user1.save()
user2 = User(username="2", password="test")
user2.save()

print(User.objects.all())

entry1 = Entry(location="location 1", subject="subject1", user=user1.id, id=user1.entry)
entry1.save()
entry2 = Entry(location="location 2", subject="subject2", user=user2.id, id=user2.entry)
entry2.save()

print(Entry.objects.all())

list_entry1 = ListEntry(entry=entry1.id)
list_entry1.save()
time.sleep(1)
list_entry2 = ListEntry(entry=entry2.id)
list_entry2.save()

conversation = Conversation(users=[str(user1.id), str(user2.id)])
conversation.save()

message1 = Message(message="Hello!", user=user1.id, conversation=conversation.id)
message1.save()

conversation.messages = conversation.messages + [str(message1.id)]
conversation.save()

