from django.shortcuts import render
from .models import Feeds, Category
from django.core.paginator import Paginator

def newsfeed(request, category_slug=None):
    if category_slug != None:
        c_id = Category.objects.get(slug=category_slug).id
        feeds= Feeds.objects.filter(category_id=c_id)
        
        paginator = Paginator(feeds, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        feeds= Feeds.objects.all()
        paginator = Paginator(feeds, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context ={
        'feeds': page_obj,
    }
    return render(request, 'feeds.html', context)

def item_detail(request,category_slug, slug):
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