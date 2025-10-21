from django.core.management.base import BaseCommand
from django.db import transaction
from django.apps import apps

# Mapping: recipe name (exact, case-sensitive as in admin) -> list of ingredient names
RECIPE_MAP = {
    "Caprese Salad": ["Tomato", "Fresh Mozzarella", "Basil", "Olive Oil"],
    "Avocado Toast": ["Avocado", "Bread", "Lemon", "Salt", "Pepper"],
    "Apple Pie": ["Apple", "Sugar", "Cinnamon", "Pie Crust"],
    "Beef and Broccoli": ["Beef Sirloin", "Broccoli", "Garlic", "Soy Sauce", "Ginger"],
    "Chicken Tikka Masala": ["Chicken Breast", "Yogurt", "Garam Masala", "Tomato Sauce"],
    "Classic Lasagna": ["Lasagna Noodles", "Marinara Sauce", "Ricotta Cheese", "Mozzarella", "Parmesan Cheese"],
    "Classic Cheeseburger": ["Ground Beef", "Burger Buns", "Lettuce", "Tomato", "Cheddar Cheese"],
    "Fluffy Pancakes": ["Flour", "Milk", "Eggs", "Sugar", "Baking Powder"],
    "Classic Tomato Soup": ["Tomato", "Onion", "Garlic", "Vegetable Broth", "Heavy Cream"],
    "French Onion Soup": ["Onion", "Beef Broth", "Gruyere Cheese", "Baguette"],
    "Garlic Butter Shrimp Pasta": ["Shrimp", "Spaghetti", "Garlic", "Butter", "Parsley"],
    "Guacamole": ["Avocado", "Lime", "Cilantro", "Onion"],
    "Macaroni and Cheese": ["Macaroni", "Cheddar Cheese", "Milk", "Butter", "Flour"],
    "Mushroom Risotto": ["Arborio Rice", "Mushroom", "Parmesan Cheese", "Vegetable Broth"],
    "Palak Paneer": ["Spinach", "Paneer", "Onion", "Garlic", "Garam Masala"],
    "Simple Lemon Herb Chicken": ["Chicken Breast", "Lemon", "Garlic", "Rosemary"],
    "Spicy Tuna Rolls": ["Sushi Rice", "Nori", "Tuna", "Sriracha"],
    "Vegetable Quiche": ["Egg", "Spinach", "Mushroom", "Cheddar Cheese", "Milk"],
    "Chicken Pad Thai": ["Rice Noodles", "Chicken Breast", "Peanuts", "Bean Sprouts", "Sriracha"],
    "Chicken Tacos": ["Chicken Breast", "Corn Tortillas", "Salsa", "Lime", "Cilantro"],
    "Chocolate Chip Cookies": ["Flour", "Sugar", "Butter", "Eggs", "Chocolate Chips"],
    "OMELETTE": ["Eggs", "Milk", "Butter"],
}

# Provide some aliasing since your Ingredient names must match exactly
ALIASES = {
    "Mozzarella": "Fresh Mozzarella",
    "Parmesan": "Parmesan Cheese",
    "Tomatoes": "Tomato",
    "Egg": "Eggs",  # admin shows both "Egg" and "Eggs"; we'll normalize to whichever exists
}

def normalize_ingredient_name(name, Ingredient):
    # prefer exact match
    obj = Ingredient.objects.filter(name=name).first()
    if obj:
        return obj
    # try alias
    alias = ALIASES.get(name)
    if alias:
        obj = Ingredient.objects.filter(name=alias).first()
        if obj:
            return obj
    # try singular/plural swaps quick-n-dirty
    if name.endswith("s"):
        obj = Ingredient.objects.filter(name=name[:-1]).first()
        if obj:
            return obj
    else:
        obj = Ingredient.objects.filter(name=name + "s").first()
        if obj:
            return obj
    return None

class Command(BaseCommand):
    help = "Links Ingredient rows to Recipe rows via RecipeIngredient for your seed recipes."

    def handle(self, *args, **opts):
        Recipe = apps.get_model("recipes", "Recipe")
        Ingredient = apps.get_model("recipes", "Ingredient")
        RecipeIngredient = apps.get_model("recipes", "RecipeIngredient")

        self.stdout.write(self.style.NOTICE("Auto-linking ingredients for seed recipes…"))

        created = 0
        skipped = 0
        with transaction.atomic():
            for rname, items in RECIPE_MAP.items():
                recipe = Recipe.objects.filter(name=rname).first()
                if not recipe:
                    self.stdout.write(self.style.WARNING(f"- Recipe not found: {rname}"))
                    continue
                for item in items:
                    ing = normalize_ingredient_name(item, Ingredient)
                    if not ing:
                        self.stdout.write(self.style.WARNING(f"  • Ingredient not found for '{item}' (recipe '{rname}')"))
                        continue
                    exists = RecipeIngredient.objects.filter(recipe=recipe, ingredient=ing).exists()
                    if exists:
                        skipped += 1
                        continue
                    # quantity left blank; you can adjust logic here if you have quantity fields
                    RecipeIngredient.objects.create(recipe=recipe, ingredient=ing)
                    created += 1

        self.stdout.write(self.style.SUCCESS(f"Done. Created {created} links; skipped {skipped} existing."))

