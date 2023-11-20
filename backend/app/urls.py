from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('submit/', views.submit, name='submit'),
    path('edit/', views.edit, name='edit'),
    path('list/', views.list_entries, name='list'),
    path('get_conversations/', views.get_conversations, name='get_conversations'),
    path('study/', views.study, name='study'),
    path('chat/', views.chat, name='chat'),
    path('get_messages/', views.get_messages, name='get_messages')
]
