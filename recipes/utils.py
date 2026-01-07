import requests
from django.conf import settings
import time

# Simple in-memory cache
_image_cache = {}
_cache_timeout = 3600  # 1 hour

def get_recipe_image_url(recipe_name):
    """
    Fetch a food image URL from Unsplash API based on recipe name.
    Returns the image URL or a placeholder if API fails.
    """
    # Check cache first
    cache_key = recipe_name.lower()
    if cache_key in _image_cache:
        cached_data = _image_cache[cache_key]
        if time.time() - cached_data['timestamp'] < _cache_timeout:
            return cached_data['url']
    
    # Get Unsplash API key from settings
    access_key = settings.UNSPLASH_ACCESS_KEY
    
    if not access_key:
        # No API key, return placeholder
        return '/static/img/no_picture.jpg'
    
    try:
        # Build search query - add food-related keywords
        query = f"{recipe_name} food dish meal"
        
        # Call Unsplash API
        url = "https://api.unsplash.com/search/photos"
        headers = {"Authorization": f"Client-ID {access_key}"}
        params = {
            "query": query,
            "per_page": 1,
            "orientation": "landscape"
        }
        
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('results') and len(data['results']) > 0:
            # Get the regular-sized image URL
            image_url = data['results'][0]['urls']['regular']
            
            # Cache it
            _image_cache[cache_key] = {
                'url': image_url,
                'timestamp': time.time()
            }
            
            return image_url
    except Exception as e:
        print(f"Unsplash API error for '{recipe_name}': {str(e)}")
    
    # Fallback to placeholder
    return '/static/img/no_picture.jpg'
