from django.db import models
from accounts.models import Accounts

class Feeds(models.Model):
    name = models.CharField(max_length=50, blank=True)
    item_name = models.CharField(max_length=25)
    item_image = models.ImageField(upload_to='images/items/', blank=True)
    category = models.CharField(max_length=25)
    location = models.CharField(max_length=35)
    time = models.CharField(max_length=20)
    descriptions = models.TextField()
    status = models.CharField(max_length=1)
    contact = models.CharField(max_length=20, blank=True)
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.item_name
