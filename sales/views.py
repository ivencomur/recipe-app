from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def home(request):
    """
    Display the home page
    """
    return render(request, 'sales/home.html')


def register_view(request):
    """
    Handle user registration
    """
    if request.user.is_authenticated:
        return redirect('recipes:list')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(
                request, 
                f'Welcome to Recipe App, {username}! Your account has been created successfully.'
            )
            return redirect('recipes:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/register.html', {'form': form})