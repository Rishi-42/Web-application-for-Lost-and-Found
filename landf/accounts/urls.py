from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
]