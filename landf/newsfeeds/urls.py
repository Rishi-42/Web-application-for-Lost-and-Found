from django.urls import path
from .views import *

urlpatterns =[
    path('', newsfeed, name='newsfeed')
]