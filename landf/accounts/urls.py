from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    
]