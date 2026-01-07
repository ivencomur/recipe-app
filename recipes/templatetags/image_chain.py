from django import template

register = template.Library()

@register.filter
def img_src_attrs(recipe):
    """Generate image src using get_image_url method"""
    # Call the model's get_image_url method which handles Unsplash
    if hasattr(recipe, 'get_image_url'):
        try:
            image_url = recipe.get_image_url()
        except Exception as e:
            print(f"Error getting image for {recipe.name}: {e}")
            image_url = '/static/img/no_picture.jpg'
    else:
        image_url = '/static/img/no_picture.jpg'
    
    fallback = '/static/img/no_picture.jpg'
    return f'src="{image_url}" onerror="this.src=\'{fallback}\'"'
