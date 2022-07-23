from django.shortcuts import render
from newsfeeds.models import Feeds
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    recent = Feeds.objects.all().order_by('-date_created')[:10]
    contexts ={
        'feeds' : recent
    }
    return render(request, 'home.html', contexts)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            feeds = Feeds.objects.order_by('-date_created').filter(Q(name__icontains=keyword) | Q(item_name__icontains=keyword) | Q(location__icontains=keyword))
            paginator = Paginator(feeds, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
    
    content = {
        'feeds': page_obj,
    }
          
    return render(request, 'result.html', content)