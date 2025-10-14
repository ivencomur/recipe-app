# sales/views.py
from django.shortcuts import render

def home(request):
    """
    Home page view for Recipe App.
    
    This is a Function-Based View (FBV) that:
    - Accepts an HttpRequest object
    - Prepares context data for the template
    - Returns an HttpResponse via render()
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
        'exercise': 'Exercise 2.4: Django Views & Templates'
    }
    
    return render(request, 'sales/recipes_home.html', context)
