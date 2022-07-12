from django.contrib import admin
from .models import Feeds, Category

class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'category', 'status', 'date_created')

admin.site.register(Feeds, FeedAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')

admin.site.register(Category, CategoryAdmin)