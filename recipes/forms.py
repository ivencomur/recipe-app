# recipes/forms.py
from django import forms

# Choices for the chart selection dropdown
CHART_CHOICES = (
    ("",  "--- Select a chart ---"), # Empty value option
    ("#1", "Bar — Recipes by Difficulty"),
    ("#2", "Pie — Cooking Time Distribution"),
    ("#3", "Line — Recipe Growth Over Time"),
)

# Choices for the difficulty filter dropdown
DIFFICULTY_CHOICES = (
    ("", "All"), 
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Hard", "Hard"),
)

class RecipeSearchForm(forms.Form):
    """
    Form for searching recipes and selecting chart type.
    """
    # Search by recipe name (optional)
    recipe_name = forms.CharField(
        max_length=120,
        required=False,
        label="Recipe Name",
        widget=forms.TextInput(attrs={"placeholder": "e.g., pasta", "class": "form-control"})
    )

    # Search by ingredients (optional, comma-separated)
    ingredients = forms.CharField(
        max_length=300,
        required=False,
        label="Ingredients (comma-separated)",
        widget=forms.TextInput(attrs={"placeholder": "e.g., tomato, cheese", "class": "form-control"})
    )

    # Filter by max cooking time (optional)
    max_cook_time = forms.IntegerField(
        required=False,
        min_value=1,
        max_value=500, # Added a max value for safety
        label="Max Cooking Time (minutes)",
        widget=forms.NumberInput(attrs={"placeholder": "30", "class": "form-control"})
    )

    # Filter by difficulty (optional dropdown)
    difficulty = forms.ChoiceField(
        choices=DIFFICULTY_CHOICES,
        required=False,
        label="Difficulty",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    # Select chart type (optional dropdown)
    chart_type = forms.ChoiceField(
        choices=CHART_CHOICES,
        required=False,
        label="Chart",
        widget=forms.Select(attrs={"class": "form-select"})
    )