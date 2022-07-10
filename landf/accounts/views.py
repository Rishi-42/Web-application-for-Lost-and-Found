from django.shortcuts import render
from .forms import RegisterForm
from .models import Accounts
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user = Accounts.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.is_active=True
            user.save()
    else:
        form = RegisterForm()
    context ={
        'form': form,
    }
    return render(request, 'register.html', context) 