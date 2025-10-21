from django import template
from django.utils.html import format_html, conditional_escape as esc
from urllib.parse import quote

register = template.Library()

@register.simple_tag
def fallback_image(recipe, width=400, height=300, cls="recipe-card-img"):
    """
    Returns an <img> that tries, in order:
      1) recipe.image.url (if present)
      2) Unsplash Source (keyworded)
      3) LoremFlickr (seeded)
      4) Picsum (seeded)
      5) Wikimedia 'No image' (final)
    Starts on a local static placeholder so there's never a broken image flash.
    """
    title = getattr(recipe, "name", "") or getattr(recipe, "title", "") or "Recipe"
    kw = quote(f"{title} food recipe")
    seed = abs(hash(title)) % 100000

    urls = []
    # local/media first
    try:
        u = getattr(getattr(recipe, "image", None), "url", None)
        if u:
            urls.append(u)
    except Exception:
        pass

    # External sources
    urls.append(f"https://source.unsplash.com/featured/{width}x{height}/?{kw}")
    urls.append(f"https://loremflickr.com/{width}/{height}/{kw}?lock={seed}")
    urls.append(f"https://picsum.photos/seed/{seed}/{width}/{height}")
    urls.append("https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg")

    # Local placeholder (shipped via staticfiles)
    placeholder = "/static/img/placeholder-recipe.svg"
    data_urls = esc("|".join(urls))

    return format_html(
        '<img class="{cls}" src="{ph}" data-fallbacks="{data}" '
        'alt="{alt}" width="{w}" height="{h}" '
        'onerror="(function(img){{'
        ' var list=(img.getAttribute(\'data-fallbacks\')||\'\').split(\'|\');'
        ' var i=parseInt(img.getAttribute(\'data-idx\')||\'0\',10);'
        ' if(i<list.length){{ img.setAttribute(\'data-idx\', i+1); img.src=list[i]; }}'
        '}})(this);" />',
        cls=esc(cls), ph=esc(placeholder), data=data_urls, alt=esc(title), w=width, h=height
    )
