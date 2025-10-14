# sales/urls.py
from django.urls import path
from .views import home

# Namespace for this app's URLs
app_name = 'sales'

urlpatterns = [
    # Route: '' (empty) maps to root when included at project level
    # View: home function from views.py
    # Name: 'home' for reverse URL lookup ({% url 'sales:home' %})
    path('', home, name='home'),
]
