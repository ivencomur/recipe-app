from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeModelsTest(TestCase):
    def setUp(self):
        self.flour = Ingredient.objects.create(name="Flour")
        self.eggs = Ingredient.objects.create(name="Eggs")

    def test_ingredient_str_and_ordering(self):
        Ingredient.objects.create(name="Basil")
        names = list(Ingredient.objects.values_list("name", flat=True))
        self.assertEqual(names, sorted(names))
        self.assertEqual(str(self.flour), "Flour")

    def test_recipe_validators(self):
        r = Recipe(name="Bad", cook_time_minutes=0)  # validator requires >= 1
        with self.assertRaises(ValidationError):
            r.full_clean()

    def test_recipeingredient_unique_pair(self):
        r = Recipe.objects.create(name="Pancakes", cook_time_minutes=10)
        RecipeIngredient.objects.create(recipe=r, ingredient=self.flour, quantity=200, unit="g")
        with self.assertRaises(IntegrityError):
            RecipeIngredient.objects.create(recipe=r, ingredient=self.flour, quantity=100, unit="g")

    def test_m2m_through_counts(self):
        r = Recipe.objects.create(name="Omelette", cook_time_minutes=5)
        RecipeIngredient.objects.create(recipe=r, ingredient=self.eggs, quantity=2, unit="")
        RecipeIngredient.objects.create(recipe=r, ingredient=self.flour, quantity=10, unit="g")
        self.assertEqual(r.ingredients.count(), 2)
        self.assertIn(r, self.eggs.recipes.all())

    def test_recipe_str(self):
        r = Recipe.objects.create(name="Tomato Soup", cook_time_minutes=30)
        self.assertEqual(str(r), "Tomato Soup")
