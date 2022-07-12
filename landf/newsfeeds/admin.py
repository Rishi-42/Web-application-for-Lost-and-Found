from django.contrib import admin
from .models import Feeds

class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'category', 'status', 'date_created')

admin.site.register(Feeds, FeedAdmin)

