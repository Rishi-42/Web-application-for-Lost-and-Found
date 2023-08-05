from django.db import models
from newsfeeds.models import Feeds
from backend.accounts.models import Accounts

class Visited(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE)
    
    viewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feed.item_name

