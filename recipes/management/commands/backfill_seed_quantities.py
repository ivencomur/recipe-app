from django.core.management.base import BaseCommand
from decimal import Decimal
from recipes.models import Recipe, Ingredient, RecipeIngredient

# Minimal, sane defaults for your 22 seed recipes
PLAN = {
    "Caprese Salad": [
        ("Tomato", 2, ""), ("Fresh Mozzarella", 8, "oz"), ("Basil", 8, "leaves"),
        ("Olive Oil", 2, "tbsp"), ("Salt", 0.5, "tsp"), ("Pepper", 0.25, "tsp"),
    ],
    "Avocado Toast": [
        ("Bread", 2, "slices"), ("Avocado", 1, ""), ("Lime", 0.5, ""),
        ("Salt", 0.25, "tsp"), ("Pepper", 0.125, "tsp"),
    ],
    "Beef and Broccoli": [
        ("Beef Sirloin", 12, "oz"), ("Broccoli", 3, "cups"), ("Garlic", 2, "cloves"),
        ("Soy Sauce", 3, "tbsp"), ("Ginger", 1, "tsp"),
    ],
    "Chicken Pad Thai": [
        ("Rice Noodles", 8, "oz"), ("Chicken Breast", 12, "oz"), ("Eggs", 2, ""),
        ("Bean Sprouts", 1, "cup"), ("Peanuts", 0.25, "cup"), ("Sriracha", 1, "tbsp"),
    ],
    "Chicken Tacos": [
        ("Chicken Breast", 12, "oz"), ("Corn Tortillas", 8, ""), ("Onion", 0.5, ""),
        ("Salsa", 0.5, "cup"), ("Cilantro", 0.25, "cup"),
    ],
    "Chicken Tikka Masala": [
        ("Chicken Breast", 16, "oz"), ("Yogurt", 0.5, "cup"), ("Garam Masala", 1, "tbsp"),
        ("Tomato Sauce", 1, "cup"), ("Garlic", 3, "cloves"), ("Ginger", 1, "tsp"),
    ],
    "Chocolate Chip Cookies": [
        ("Flour", 2.25, "cups"), ("Sugar", 0.75, "cup"), ("Brown Sugar", 0.75, "cup"),
        ("Butter", 1, "cup"), ("Egg", 2, ""), ("Chocolate Chips", 2, "cups"),
        ("Baking Powder", 1, "tsp"),
    ],
    "Classic Cheeseburger": [
        ("Ground Beef", 16, "oz"), ("Burger Buns", 4, ""), ("Cheddar Cheese", 4, "slices"),
        ("Lettuce", 4, "leaves"), ("Onion", 0.5, ""), ("Tomato", 1, ""),
    ],
    "Classic Lasagna": [
        ("Lasagna Noodles", 12, ""), ("Marinara Sauce", 3, "cups"), ("Ricotta Cheese", 15, "oz"),
        ("Fresh Mozzarella", 8, "oz"), ("Parmesan Cheese", 0.5, "cup"),
    ],
    "Classic Tomato Soup": [
        ("Tomato", 6, ""), ("Onion", 1, ""), ("Garlic", 2, "cloves"),
        ("Olive Oil", 1, "tbsp"), ("Vegetable Broth", 3, "cups"),
    ],
    "Fluffy Pancakes": [
        ("Flour", 1.5, "cups"), ("Milk", 1.25, "cups"), ("Egg", 1, ""),
        ("Baking Powder", 3.5, "tsp"), ("Sugar", 1, "tbsp"), ("Butter", 2, "tbsp"),
    ],
    "French Onion Soup": [
        ("Onion", 4, ""), ("Butter", 3, "tbsp"), ("Beef Broth", 6, "cups"),
        ("Gruyere Cheese", 6, "oz"), ("Baguette", 8, "slices"), ("Thyme", 0.5, "tsp"),
    ],
    "Garlic Butter Shrimp Pasta": [
        ("Shrimp", 12, "oz"), ("Spaghetti", 8, "oz"), ("Butter", 3, "tbsp"),
        ("Garlic", 3, "cloves"), ("Parsley", 2, "tbsp"),
    ],
    "Guacamole": [
        ("Avocado", 3, ""), ("Onion", 0.25, ""), ("Tomato", 1, ""),
        ("Lime", 1, ""), ("Cilantro", 2, "tbsp"), ("Salt", 0.5, "tsp"),
    ],
    "Macaroni and Cheese": [
        ("Macaroni", 8, "oz"), ("Milk", 2, "cups"), ("Butter", 2, "tbsp"),
        ("Cheddar Cheese", 2, "cups"), ("Flour", 2, "tbsp"),
    ],
    "Mushroom Risotto": [
        ("Arborio Rice", 1.5, "cups"), ("Mushroom", 12, "oz"), ("Onion", 1, ""),
        ("Parmesan Cheese", 0.75, "cup"), ("Vegetable Broth", 5, "cups"),
        ("Butter", 2, "tbsp"),
    ],
    "OMELETTE": [
        ("Eggs", 3, ""), ("Milk", 2, "tbsp"), ("Butter", 1, "tbsp"),
        ("Cheddar Cheese", 0.5, "cup"),
    ],
    "Palak Paneer": [
        ("Spinach", 12, "oz"), ("Paneer", 12, "oz"), ("Onion", 1, ""), ("Garlic", 3, "cloves"),
        ("Garam Masala", 1, "tsp"), ("Yogurt", 0.25, "cup"),
    ],
    "Simple Lemon Herb Chicken": [
        ("Chicken Breast", 16, "oz"), ("Lemon", 1, ""), ("Olive Oil", 2, "tbsp"),
        ("Rosemary", 1, "tsp"), ("Thyme", 1, "tsp"),
    ],
    "Spicy Tuna Rolls": [
        ("Sushi Rice", 2, "cups"), ("Nori", 4, "sheets"), ("Tuna", 8, "oz"),
        ("Sriracha", 1, "tbsp"),
    ],
    "Vegetable Quiche": [
        ("Eggs", 4, ""), ("Milk", 1, "cup"), ("Spinach", 2, "cups"),
        ("Mushroom", 1, "cup"), ("Pie Crust", 1, ""),
    ],
    "Apple Pie": [
        ("Apple", 6, ""), ("Sugar", 0.75, "cup"), ("Cinnamon", 1, "tsp"),
        ("Pie Crust", 1, ""),
    ],
}

class Command(BaseCommand):
    help = "Backfill quantities and units for seed RecipeIngredients."

    def handle(self, *args, **opts):
        created_or_updated = 0
        missing_ingredients = set()

        for recipe_name, items in PLAN.items():
            try:
                recipe = Recipe.objects.get(name=recipe_name)
            except Recipe.DoesNotExist:
                self.stdout.write(f"Recipe not found: {recipe_name}")
                continue

            for ing_name, qty, unit in items:
                ing = Ingredient.objects.filter(name=ing_name).first()
                if not ing:
                    missing_ingredients.add(ing_name)
                    continue

                ri, _ = RecipeIngredient.objects.get_or_create(recipe=recipe, ingredient=ing)
                ri.quantity = Decimal(str(qty))
                ri.unit = unit
                ri.save(update_fields=["quantity", "unit"])
                created_or_updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Done. Set quantities/units on {created_or_updated} recipe-ingredient rows."
        ))
        if missing_ingredients:
            self.stdout.write("Missing Ingredient rows for: " + ", ".join(sorted(missing_ingredients)))
