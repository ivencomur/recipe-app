from django import template
from django.conf import settings
from urllib.parse import quote
register = template.Library()

def _media_url():
    mu = getattr(settings, "MEDIA_URL", "/media/")
    if not mu.startswith("/"):
        mu = "/" + mu.lstrip("/")
    if not mu.endswith("/"):
        mu += "/"
    return mu

def normalize_url(name_or_url):
    if not name_or_url:
        return ""
    v = str(name_or_url)
    if v.lower().startswith(("http://","https://")) or v.startswith("/"):
        return v
    return _media_url() + v.lstrip("/")

@register.filter
def img_src_attrs(recipe):
    title = getattr(recipe, "name", "") or "recipe"
    q = quote(title)
    primary = ""
    img = getattr(recipe, "image", None)
    if img:
        primary = normalize_url(getattr(img, "url", None) or getattr(img, "name", ""))
    chain = [
        f"https://source.unsplash.com/featured/400x300?{q}",
        f"https://loremflickr.com/400/300/{q}",
        f"https://picsum.photos/seed/{q}/400/300",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Plate_with_food_icon.svg/640px-Plate_with_food_icon.svg.png",
    ]
    urls = ([primary] if primary else []) + chain
    src = urls[0] if urls else "/static/img/placeholder-recipe.svg"
    data = "|".join(urls[1:]) if len(urls) > 1 else ""
    return f'src="{src}" data-srcs="{data}"'
