# recipes/urls.py

from django.urls import path
# Import all necessary views from the views module
from .views import RecipeListView, RecipeDetailView, recipe_search

app_name = 'recipes' # Define the namespace for this app

urlpatterns = [
    # Path for the recipe list page (e.g., /recipes/)
    path('', RecipeListView.as_view(), name='list'),

    # Path for the recipe search page (e.g., /recipes/search/) - NEW
    path('search/', recipe_search, name='search'),

    # Path for the recipe detail page (e.g., /recipes/1/)
   
    path('<int:pk>/', RecipeDetailView.as_view(), name='detail'),

    # but your views.py uses a Class-Based View RecipeDetailView.
 
]