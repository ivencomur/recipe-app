# recipe_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),
    
    # Root URL (http://127.0.0.1:8000/) -> delegate to sales app
    path('', include('sales.urls')),
]
