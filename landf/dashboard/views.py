from ast import Add
from unicodedata import category
from django.shortcuts import render, redirect
from .forms import AddPostForm
from newsfeeds.models import Feeds
from accounts.models import Accounts

def dashboard(request):
    return render(request, 'add_feed.html')
    
def add_post(request):
    current_user = request.user.id
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            item_image = form.cleaned_data['item_image']
            name = form.cleaned_data['name']
            status = form.cleaned_data['status']
            location = form.cleaned_data['location']
            time = form.cleaned_data['time']
            category = form.cleaned_data['category']
            contact = form.cleaned_data['contact']
            descriptions=form.cleaned_data['descriptions']
            
            feed = Feeds(item_name=item_name, item_image=item_image, name=name, status = status, time =time, contact=contact, category=category, location=location, descriptions=descriptions, user = Accounts.objects.get(id=current_user))
            feed.save()

            return redirect('home')
    else:
        form = AddPostForm()
    
    contexts = {
        'form': form,
    }
    return render(request, 'add_feed.html', contexts)