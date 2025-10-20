# recipes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Ingredient, RecipeIngredient

# Ex 2.7: Search & Charts
# Need login for search view
from django.contrib.auth.decorators import login_required
# For OR filter (Q) and counting (Count)
from django.db.models import Q, Count
# The search form we made
from .forms import RecipeSearchForm
# For charts - data handling
import pandas as pd
# For charts - image buffer
from io import BytesIO
# For charts - image encoding
import base64
# For charts - plotting library
import matplotlib
# For charts - IMPORTANT: use 'Agg' backend for servers (no GUI)
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Chart Helper Function (Ex 2.7)
def generate_recipe_chart(chart_type, qs, df=None):
    """Makes the chart image based on search results."""

    # Don't plot if no chart type selected or no recipes found
    if not chart_type or not qs.exists():
        return None

    # Use 'Agg' backend again just to be safe
    plt.switch_backend("Agg")
    # Set up the plot area
    fig, ax = plt.subplots(figsize=(10, 6))

    try:
        # Chart #1: Bar chart for difficulty
        if chart_type == "#1":
            # Count recipes per difficulty
            data = list(qs.values("difficulty").annotate(count=Count("difficulty")).order_by('difficulty'))
            # Need data to plot
            if not data: return None
            # Plotting
            pdf = pd.DataFrame(data)
            ax.bar(pdf["difficulty"], pdf["count"], color=['#1f77b4', '#ff7f0e', '#2ca02c'])
            ax.set_xlabel("Difficulty Level")
            ax.set_ylabel("Number of Recipes")
            ax.set_title("Recipes by Difficulty")

        # Chart #2: Pie chart for cooking time
        elif chart_type == "#2":
            # Get all cook times
            times = list(qs.values_list("cook_time_minutes", flat=True))
            # Remove any nulls
            times = [t for t in times if t is not None]
            # Need times to plot
            if not times: return None

            # Group times into buckets
            buckets = {
                "≤ 30 min": sum(1 for t in times if t <= 30),
                "31–60 min": sum(1 for t in times if 30 < t <= 60),
                "> 60 min": sum(1 for t in times if t > 60),
            }
            # Remove empty buckets so pie chart looks clean
            buckets = {k: v for k, v in buckets.items() if v > 0}
            # Need buckets with data
            if not buckets: return None
            # Plotting
            ax.pie(buckets.values(), labels=buckets.keys(), autopct="%1.1f%%", startangle=90)
            ax.set_title("Cooking Time Distribution")
            # Make it a circle
            ax.axis('equal')

        # Chart #3: Line chart for recipe growth
        elif chart_type == "#3":
            # Use DataFrame if passed in, else make one
            if df is None:
                df = pd.DataFrame(qs.values("created_at"))

            # Need 'created_at' dates to plot
            if "created_at" not in df.columns or df["created_at"].isna().all():
                return None

            # Convert to date objects
            df["created_at"] = pd.to_datetime(df["created_at"])
            # Sort by date
            df = df.sort_values("created_at")
            # Add cumulative count column (1, 2, 3...)
            df["cumulative"] = range(1, len(df) + 1)
            # Plotting
            ax.plot(df["created_at"], df["cumulative"], marker="o", linestyle='-')
            ax.set_xlabel("Date Added")
            ax.set_ylabel("Total Number of Recipes")
            ax.set_title("Recipe Collection Growth Over Time")
            # Rotate date labels so they don't overlap
            plt.xticks(rotation=45, ha='right')

        else:
            # Unknown chart type
            return None

        # Convert plot to image string
        # Fit plot correctly
        plt.tight_layout()
        # Temporary memory buffer for image
        buf = BytesIO()
        # Save plot PNG into buffer
        plt.savefig(buf, format="png", dpi=100, bbox_inches="tight")
        # Go back to start of buffer
        buf.seek(0)
        # Encode image bytes as base64 text
        img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        # Free memory
        buf.close()
        plt.close(fig)
        # Send back the image text
        return img_b64

    except Exception as e:
        # If something went wrong during plotting
        print(f"Error generating chart {chart_type}: {e}")
        # Clean up plot figure
        plt.close(fig)
        return None


# Search View Function (Ex 2.7)
# User must be logged in to see this page
@login_required
def recipe_search(request):
    """Handles search form and shows results + charts."""

    # Create form instance - use POST data if submitted, else empty form
    form = RecipeSearchForm(request.POST or None)
    # Start with no results or chart
    recipes = None
    chart = None

    # If form was submitted (POST request)
    if request.method == "POST":

        # Special case: "Show All" button pressed
        if "show_all" in request.POST:
            recipes = Recipe.objects.all().order_by("name")

        # Regular search form submitted and valid
        elif form.is_valid():
            # Start query with all recipes
            qs = Recipe.objects.all()

            # Get the (cleaned) search terms from the form
            name_query = form.cleaned_data.get("recipe_name")
            ingredients_query = form.cleaned_data.get("ingredients")
            max_time_query = form.cleaned_data.get("max_cook_time")
            difficulty_query = form.cleaned_data.get("difficulty")
            chart_type_query = form.cleaned_data.get("chart_type")

            # Apply filters if user entered terms
            # Filter by name (partially matches, ignore case)
            if name_query:
                qs = qs.filter(name__icontains=name_query)

            # Filter by ingredients (comma-separated, any match, ignore case)
            if ingredients_query:
                # Get list of ingredients entered
                terms = [term.strip() for term in ingredients_query.split(",") if term.strip()]
                if terms:
                    # Build OR query using Q objects
                    query = Q()
                    for term in terms:
                        # Check ingredient *names* via the relationship
                        query |= Q(ingredients__name__icontains=term)
                    # Apply filter, remove duplicates if a recipe matches >1 term
                    qs = qs.filter(query).distinct()

            # Filter by max cooking time (less than or equal)
            if max_time_query:
                qs = qs.filter(cook_time_minutes__lte=max_time_query)

            # Filter by difficulty (exact match)
            if difficulty_query:
                qs = qs.filter(difficulty=difficulty_query)

            # Final results, sorted by name
            recipes = qs.order_by("name")

            # Try generating chart if requested AND we found recipes
            if recipes.exists() and chart_type_query:
                # Make DataFrame needed for chart #3 efficiently
                df = pd.DataFrame(recipes.values("created_at", "cook_time_minutes", "difficulty"))
                chart = generate_recipe_chart(chart_type_query, recipes, df=df)

    # Data to send to the template
    context = {
        "form": form,
        "recipes": recipes,
        "chart": chart,
    }
    # Load the search.html page with the context data
    return render(request, "recipes/search.html", context)


# Existing Class-Based Views
# Shows list of all recipes
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

# Shows details of one recipe
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'