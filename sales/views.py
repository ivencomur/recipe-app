# sales/views.py
from django.shortcuts import render

def home(request):
    """
    Home page view for Recipe App.
    """
    context = {
        'app_name': 'Recipe Collection',
        'tagline': 'Organize, Cook, and Share Your Favorite Recipes',
        'features': [
            'Store unlimited recipes',
            'Track cooking times and difficulty',
            'Search and filter your collection',
            'Share recipes with friends'
        ],
        'exercise': 'Exercise 2.6: User Authentication' # Updated exercise name
    }

    return render(request, 'sales/recipes_home.html', context)