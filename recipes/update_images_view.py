from django.http import HttpResponse
from recipes.models import Recipe
from recipes.utils import get_recipe_image_url

def update_images_view(request):
    output = []
    recipes = Recipe.objects.all()
    
    for recipe in recipes:
        try:
            unsplash_url = get_recipe_image_url(recipe.name)
            recipe.pic = unsplash_url
            recipe.save()
            output.append(f"✅ Updated {recipe.name}<br>")
        except Exception as e:
            output.append(f"❌ Error updating {recipe.name}: {str(e)}<br>")
    
    output.append(f"<br><b>Done! Updated {len(recipes)} recipes</b>")
    return HttpResponse("".join(output))
