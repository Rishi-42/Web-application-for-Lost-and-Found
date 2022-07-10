from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('signin/', signin, name='signin'),
    path('home/', home, name='home' ),
    
]