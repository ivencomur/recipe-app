# sales/urls.py

from django.urls import path
from .views import home  # Make sure 'home' is defined in sales/views.py
from . import views 

app_name = 'sales'

urlpatterns = [
    # This file should ONLY define the path for the homepage within the sales app.
    path('', home, name='home'),
    path('register/', views.register_view, name='register'),
]