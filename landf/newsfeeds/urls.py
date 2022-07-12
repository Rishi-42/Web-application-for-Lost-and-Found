from django.urls import path
from .views import *

urlpatterns =[
    path('', newsfeed, name='newsfeed'),
    path('<slug>', item_detail, name='item_detail'),
]