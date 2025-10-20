# recipes/tests/test_forms.py

from django.test import TestCase
# Import the form we want to test
from recipes.forms import RecipeSearchForm

class RecipeSearchFormTest(TestCase):

    # Test if all expected fields are present in the form
    def test_fields_present(self):
        form = RecipeSearchForm()
        # Check if the keys match exactly the fields we defined
        self.assertEqual(
            list(form.fields.keys()),
            ["recipe_name", "ingredients", "max_cook_time", "difficulty", "chart_type"],
        )
        # Check field labels match what we set
        self.assertEqual(form.fields['recipe_name'].label, "Recipe Name")
        self.assertEqual(form.fields['ingredients'].label, "Ingredients (comma-separated)")
        self.assertEqual(form.fields['max_cook_time'].label, "Max Cooking Time (minutes)")
        self.assertEqual(form.fields['difficulty'].label, "Difficulty")
        self.assertEqual(form.fields['chart_type'].label, "Chart")

    # Test if an empty form (no data submitted) is considered valid
    # Since all fields are required=False, this should pass
    def test_empty_form_is_valid(self):
        form = RecipeSearchForm(data={})
        self.assertTrue(form.is_valid())

    # Test if submitting only some fields is valid
    def test_partial_data_is_valid(self):
        form = RecipeSearchForm(data={"recipe_name": "pasta"})
        self.assertTrue(form.is_valid())
        form = RecipeSearchForm(data={"max_cook_time": 60})
        self.assertTrue(form.is_valid())
        form = RecipeSearchForm(data={"difficulty": "Easy"})
        self.assertTrue(form.is_valid())

    # Test the validation for the max_cook_time field
    def test_max_cook_time_validation(self):
        # Test lower bound (min_value=1)
        form_invalid_min = RecipeSearchForm(data={"max_cook_time": 0})
        self.assertFalse(form_invalid_min.is_valid())
        self.assertIn('max_cook_time', form_invalid_min.errors)

        # Test upper bound (max_value=500)
        form_invalid_max = RecipeSearchForm(data={"max_cook_time": 501})
        self.assertFalse(form_invalid_max.is_valid())
        self.assertIn('max_cook_time', form_invalid_max.errors)

        # Test a valid value within bounds
        form_valid = RecipeSearchForm(data={"max_cook_time": 30})
        self.assertTrue(form_valid.is_valid())

    # Test that non-integer input for max_cook_time fails
    def test_max_cook_time_non_integer(self):
        form = RecipeSearchForm(data={"max_cook_time": "thirty"})
        self.assertFalse(form.is_valid())
        self.assertIn('max_cook_time', form.errors)