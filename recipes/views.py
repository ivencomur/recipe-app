# recipes/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
# ADD THIS LINE to import the protection mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

# Your classes should now work correctly
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'