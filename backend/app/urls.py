from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('submit/', views.submit, name='submit'),
    path('edit/', views.edit, name='edit'),
    path('list/', views.list, name='list')
]
