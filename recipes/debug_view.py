from django.http import HttpResponse
from recipes.models import Recipe

def debug_images(request):
    output = []
    recipes = Recipe.objects.all()[:5]
    
    for recipe in recipes:
        pic_value = str(recipe.pic) if recipe.pic else ''
        output.append(f"<h3>{recipe.name}</h3>")
        output.append(f"<p>DB value: {pic_value}</p>")
        output.append(f"<p>Contains 'recipes/': {'recipes/' in pic_value}</p>")
        output.append(f"<p>Ends with image ext: {pic_value.endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif'))}</p>")
        output.append(f"<p>get_image_url() returns: {recipe.get_image_url()}</p>")
        output.append("<hr>")
    
    return HttpResponse(''.join(output))
