from django.urls import path
from .views import *

urlpatterns =[
    path('', newsfeed, name='newsfeed'),
    path('<slug:category_slug>', newsfeed, name='category_product'),
    path('<slug:category_slug>/<slug>', item_detail, name='item_detail'),
]