from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    """Display the home page"""
    return render(request, 'sales/home.html')

def register_view(request):
    """Handle user registration"""
    if request.user.is_authenticated:
        return redirect('recipes:list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes:list')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/register.html', {'form': form})
