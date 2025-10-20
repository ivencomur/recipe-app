# recipes/tests/test_views.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# Import the model needed for creating test data
from recipes.models import Recipe, Ingredient # Import Ingredient if needed for setup

class RecipeSearchViewTest(TestCase):

    # Set up initial data for all tests in this class
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username="testuser", password="password123")

        # Create some test ingredients (if using ManyToManyField correctly)
        # Ingredient names should match those used below if creating RecipeIngredient directly
        Ingredient.objects.create(name="Pasta")
        Ingredient.objects.create(name="Eggs")
        Ingredient.objects.create(name="Bacon")
        Ingredient.objects.create(name="Flour")
        Ingredient.objects.create(name="Tomato")
        Ingredient.objects.create(name="Mozzarella")
        Ingredient.objects.create(name="Beef")
        Ingredient.objects.create(name="Mushrooms")
        Ingredient.objects.create(name="Pastry")

        # Create test recipes with different attributes
        # Note: If using ManyToManyField, you add ingredients *after* creating the Recipe object.
        cls.recipe1 = Recipe.objects.create(
            name="Pasta Carbonara",
            # Assuming ingredients are linked via M2M, not a text field
            # description="Classic Italian pasta", # Add description if needed
            cook_time_minutes=25,
            difficulty="Easy",
        )
        cls.recipe1.ingredients.add(Ingredient.objects.get(name="Pasta"))
        cls.recipe1.ingredients.add(Ingredient.objects.get(name="Eggs"))
        cls.recipe1.ingredients.add(Ingredient.objects.get(name="Bacon"))

        cls.recipe2 = Recipe.objects.create(
            name="Pizza Margherita",
            cook_time_minutes=45,
            difficulty="Medium",
        )
        cls.recipe2.ingredients.add(Ingredient.objects.get(name="Flour"))
        cls.recipe2.ingredients.add(Ingredient.objects.get(name="Tomato"))
        cls.recipe2.ingredients.add(Ingredient.objects.get(name="Mozzarella"))

        cls.recipe3 = Recipe.objects.create(
            name="Beef Wellington",
            cook_time_minutes=120,
            difficulty="Hard",
        )
        cls.recipe3.ingredients.add(Ingredient.objects.get(name="Beef"))
        cls.recipe3.ingredients.add(Ingredient.objects.get(name="Mushrooms"))
        cls.recipe3.ingredients.add(Ingredient.objects.get(name="Pastry"))

    # Set up the test client and URL for each individual test method
    def setUp(self):
        self.client = Client()
        # Get the URL for the search page using its name
        self.url = reverse("recipes:search")

    # Test that accessing the search page redirects to login if not authenticated
    def test_search_view_requires_login(self):
        response = self.client.get(self.url)
        # Expecting a redirect (status code 302)
        self.assertEqual(response.status_code, 302)
        # Check it redirects to the login URL (uses LOGIN_URL from settings)
        self.assertRedirects(response, f'/login/?next={self.url}')

    # Test that an authenticated user can access the search page (GET request)
    def test_search_view_get_request_authenticated(self):
        # Log in the test user
        self.client.login(username="testuser", password="password123")
        response = self.client.get(self.url)
        # Expecting success (status code 200)
        self.assertEqual(response.status_code, 200)
        # Check if the page title or a key heading is present
        self.assertContains(response, "Recipe Search & Analytics")
        # Check if the form is present in the context
        self.assertIn('form', response.context)

    # Test searching by partial recipe name
    def test_search_by_partial_name(self):
        self.client.login(username="testuser", password="password123")
        # Simulate POST request with form data
        response = self.client.post(self.url, {"recipe_name": "Piz"})
        self.assertEqual(response.status_code, 200)
        # Check that the correct recipe is found and others are not
        self.assertContains(response, "Pizza Margherita")
        self.assertNotContains(response, "Pasta Carbonara")
        self.assertNotContains(response, "Beef Wellington")
        # Check results count if needed
        self.assertEqual(len(response.context['recipes']), 1)

    # Test searching by ingredients using OR logic
    def test_search_by_ingredients_or_logic(self):
        self.client.login(username="testuser", password="password123")
        # Search for recipes containing either 'mozzarella' OR 'bacon'
        response = self.client.post(self.url, {"ingredients": "mozzarella, bacon"})
        self.assertEqual(response.status_code, 200)
        # Check that both relevant recipes appear
        self.assertContains(response, "Pizza Margherita")  # Has mozzarella
        self.assertContains(response, "Pasta Carbonara")   # Has bacon
        self.assertNotContains(response, "Beef Wellington") # Has neither
        self.assertEqual(len(response.context['recipes']), 2)

    # Test filtering by maximum cooking time
    def test_search_by_max_cook_time(self):
        self.client.login(username="testuser", password="password123")
        # Search for recipes taking 30 minutes or less
        response = self.client.post(self.url, {"max_cook_time": 30})
        self.assertEqual(response.status_code, 200)
        # Only Carbonara should match
        self.assertContains(response, "Pasta Carbonara")
        self.assertNotContains(response, "Pizza Margherita")
        self.assertNotContains(response, "Beef Wellington")
        self.assertEqual(len(response.context['recipes']), 1)

    # Test filtering by difficulty
    def test_search_by_difficulty(self):
        self.client.login(username="testuser", password="password123")
        # Search for 'Easy' recipes
        response = self.client.post(self.url, {"difficulty": "Easy"})
        self.assertEqual(response.status_code, 200)
        # Only Carbonara should match
        self.assertContains(response, "Pasta Carbonara")
        self.assertNotContains(response, "Pizza Margherita")
        self.assertNotContains(response, "Beef Wellington")
        self.assertEqual(len(response.context['recipes']), 1)

        # Search for 'Hard' recipes
        response_hard = self.client.post(self.url, {"difficulty": "Hard"})
        self.assertEqual(response_hard.status_code, 200)
        self.assertContains(response_hard, "Beef Wellington")
        self.assertNotContains(response_hard, "Pasta Carbonara")
        self.assertEqual(len(response_hard.context['recipes']), 1)

    # Test the "Show All" button functionality
    def test_show_all_button(self):
        self.client.login(username="testuser", password="password123")
        # Simulate POST request with 'show_all' parameter
        response = self.client.post(self.url, {"show_all": "true"})
        self.assertEqual(response.status_code, 200)
        # Check that all recipes are present
        self.assertContains(response, "Pasta Carbonara")
        self.assertContains(response, "Pizza Margherita")
        self.assertContains(response, "Beef Wellington")
        self.assertEqual(len(response.context['recipes']), 3) # Should show all 3 recipes

    # Optional: Test that chart context is None when no chart type selected
    def test_chart_context_is_none_by_default(self):
        self.client.login(username="testuser", password="password123")
        # POST without selecting chart_type
        response = self.client.post(self.url, {"recipe_name": "Pasta"})
        self.assertEqual(response.status_code, 200)
        # Check that 'chart' key in context is None
        self.assertIsNone(response.context.get('chart'))

    # Optional: Test chart generation (basic check if chart data is present)
    # Note: This doesn't validate the image content, just that *something* was generated
    def test_chart_generation_context_present(self):
        self.client.login(username="testuser", password="password123")
        # POST with a chart type selected
        response = self.client.post(self.url, {"recipe_name": "P", "chart_type": "#1"}) # Search for 'P' (Pasta, Pizza), request chart #1
        self.assertEqual(response.status_code, 200)
        # Check that 'chart' key exists and is not None (should be a base64 string)
        self.assertIsNotNone(response.context.get('chart'))
        self.assertIsInstance(response.context.get('chart'), str)
        self.assertTrue(len(response.context.get('chart')) > 100) # Check it's a reasonably long base64 string