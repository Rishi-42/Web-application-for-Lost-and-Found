from django.shortcuts import render
from .models import Feeds

def newsfeed(request):
    feeds= Feeds.objects.all()
    context ={
        'feeds': feeds,
    }
    return render(request, 'feeds.html', context)

def item_detail(request, slug):
    feed_detail = Feeds.objects.get(slug=slug)
    feed_detail_id = feed_detail.id
    item_category=feed_detail.category.id
    similar_items = Feeds.objects.filter(category=item_category)
    similar_items= similar_items.exclude(id=feed_detail_id)
    context ={
        'feed_detail' : feed_detail, 
        'similar_items' : similar_items,
    }
    return render(request, 'feed_details.html', context)