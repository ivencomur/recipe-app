# recipes/tests.py

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeModelsTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by multiple test methods
        self.flour = Ingredient.objects.create(name="Flour")
        self.eggs = Ingredient.objects.create(name="Eggs")
        # Add difficulty to recipes created in tests where needed
        self.recipe_pancakes = Recipe.objects.create(name="Pancakes", cook_time_minutes=10, difficulty="Easy")
        self.recipe_omelette = Recipe.objects.create(name="Omelette", cook_time_minutes=5, difficulty="Easy")
        self.recipe_soup = Recipe.objects.create(name="Tomato Soup", cook_time_minutes=30, difficulty="Medium")

    def test_ingredient_str_and_ordering(self):
        # Test string representation and default ordering
        Ingredient.objects.create(name="Basil")
        names = list(Ingredient.objects.values_list("name", flat=True))
        self.assertEqual(names, sorted(names)) # Check if names are sorted alphabetically
        self.assertEqual(str(self.flour), "Flour")

    def test_recipe_validators(self):
        # Test PositiveIntegerField validator for cook_time_minutes (must be >= 1)
        # Create recipe instance without saving to test full_clean
        r = Recipe(name="Bad Time", cook_time_minutes=0, difficulty="Easy")
        # full_clean() runs model validation
        with self.assertRaises(ValidationError):
            r.full_clean()

    def test_recipeingredient_unique_pair(self):
        # Test unique_together constraint on RecipeIngredient (recipe, ingredient)
        # First ingredient is okay
        RecipeIngredient.objects.create(recipe=self.recipe_pancakes, ingredient=self.flour, quantity=200, unit="g")
        # Adding the same ingredient again should raise IntegrityError
        with self.assertRaises(IntegrityError):
            RecipeIngredient.objects.create(recipe=self.recipe_pancakes, ingredient=self.flour, quantity=100, unit="g")

    def test_m2m_through_counts(self):
        # Test ManyToManyField relationship via RecipeIngredient
        RecipeIngredient.objects.create(recipe=self.recipe_omelette, ingredient=self.eggs, quantity=2, unit="")
        RecipeIngredient.objects.create(recipe=self.recipe_omelette, ingredient=self.flour, quantity=10, unit="g")
        # Check count using the forward relationship (Recipe -> Ingredients)
        self.assertEqual(self.recipe_omelette.ingredients.count(), 2)
        # Check count using the reverse relationship (Ingredient -> Recipes)
        self.assertEqual(self.eggs.recipes.count(), 1)
        self.assertIn(self.recipe_omelette, self.eggs.recipes.all())

    def test_recipe_str(self):
        # Test string representation of Recipe model
        self.assertEqual(str(self.recipe_soup), "Tomato Soup")

    def test_get_absolute_url(self):
        # Test the get_absolute_url method on the Recipe model
        # Create a specific recipe for this test
        # Add the missing difficulty and closing parenthesis
        recipe_for_url = Recipe.objects.create(name="Test Cake URL", cook_time_minutes=30, difficulty="Medium")
        # Assert that the method returns the expected URL WITH the trailing slash
        # Django automatically assigns primary keys, to rely on its behavior here.
    
        # We use the object's actual pk attribute for robustness.
        expected_url = f'/recipes/{recipe_for_url.pk}/'
        self.assertEqual(recipe_for_url.get_absolute_url(), expected_url) # <<< Use f-string and expect trailing slash