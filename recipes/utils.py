# recipes/utils.py
import requests
from django.conf import settings
import time

# Simple cache to avoid repeated API calls
_image_cache = {}
_cache_timeout = 3600  # 1 hour

def get_recipe_image_url(recipe_name):
    '''
    Fetch a food image from Unsplash API based on recipe name.
    Returns image URL or default placeholder if API fails.
    '''
    if not getattr(settings, 'UNSPLASH_ACCESS_KEY', None):
        return '/static/img/no_picture.jpg'
    
    # Check cache first
    cache_key = recipe_name.lower().strip()
    if cache_key in _image_cache:
        cached_data = _image_cache[cache_key]
        if time.time() - cached_data['timestamp'] < _cache_timeout:
            return cached_data['url']
    
    try:
        url = 'https://api.unsplash.com/search/photos'
        params = {
            'query': f'{recipe_name} food dish meal',
            'per_page': 1,
            'orientation': 'landscape',
            'client_id': settings.UNSPLASH_ACCESS_KEY
        }
        
        response = requests.get(url, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('results') and len(data['results']) > 0:
                image_url = data['results'][0]['urls']['regular']
                _image_cache[cache_key] = {
                    'url': image_url,
                    'timestamp': time.time()
                }
                return image_url
    
    except Exception as e:
        print(f'Error fetching image for {recipe_name}: {e}')
    
    return '/static/img/no_picture.jpg'

def clear_image_cache():
    '''Clear the image URL cache'''
    global _image_cache
    _image_cache = {}
