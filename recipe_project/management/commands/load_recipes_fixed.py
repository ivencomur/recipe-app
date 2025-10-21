import json
from django.core.management.base import BaseCommand
from recipes.models import Ingredient, Recipe

class Command(BaseCommand):
    help = 'Load recipes data with proper encoding handling'

    def handle(self, *args, **options):
        # Read JSON with Latin-1 encoding and convert to UTF-8
        with open('recipes_data.json', 'rb') as f:
            content = f.read().decode('latin-1')
        
        # Parse the JSON
        data = json.loads(content)
        
        loaded_count = 0
        for obj in data:
            model = obj['model']
            fields = obj['fields']
            pk = obj['pk']
            
            try:
                if model == 'recipes.ingredient':
                    Ingredient.objects.get_or_create(pk=pk, defaults=fields)
                    loaded_count += 1
                elif model == 'recipes.recipe':
                    Recipe.objects.get_or_create(pk=pk, defaults=fields)
                    loaded_count += 1
            except Exception as e:
                self.stdout.write(f"Error loading {model} {pk}: {e}")
        
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {loaded_count} objects'))
