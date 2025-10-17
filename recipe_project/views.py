# recipe_project/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    """
    Handles user login.
    """
    error_message = None
    # Unbound form for a GET request
    form = AuthenticationForm()

    if request.method == 'POST':
        # Form bound with user's POST data
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log the user in and redirect to the recipe list
                login(request, user)
                return redirect('recipes:list')
        else:
            # If the form is invalid, set an error message
            error_message = 'Invalid username or password.'

    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'auth/login.html', context)

def logout_view(request):
    """
    Handles user logout.
    """
    logout(request)
    # Redirect to a dedicated "logged out" page
    return redirect('logout_success')

def logout_success_view(request):
    """
    Displays a success message after the user logs out.
    """
    return render(request, 'auth/logout_success.html')