# recipes/urls.py

from django.urls import path
from .views import RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    # Example: /recipes/
    path('', RecipeListView.as_view(), name='list'),

    # Example: /recipes/1/
    path('<pk>', RecipeDetailView.as_view(), name='detail'),
]