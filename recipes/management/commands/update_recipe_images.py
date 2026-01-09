from django.core.management.base import BaseCommand
from recipes.models import Recipe
from recipes.utils import get_recipe_image_url

class Command(BaseCommand):
    help = 'Update all recipe images to use Unsplash URLs'

    def handle(self, *args, **kwargs):
        recipes = Recipe.objects.all()
        updated = 0
        
        for recipe in recipes:
            # Get Unsplash URL
            unsplash_url = get_recipe_image_url(recipe.name)
            
            # Update the pic field directly
            recipe.pic = unsplash_url
            recipe.save()
            
            updated += 1
            self.stdout.write(f"Updated {recipe.name}: {unsplash_url}")
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated} recipes'))
