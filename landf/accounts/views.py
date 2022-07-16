from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Accounts
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
            user.is_active = True
            user.save()
            messages.success(
                request, 'Account is activated.'
            )
            return redirect('signin')
    else:
        form = RegisterForm()
    context ={
        'form': form,
    }
    return render(request, 'register.html', context) 

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'signin.html')
    return render(request, 'signin.html')


@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out.')
    return render(request, 'signin.html')


