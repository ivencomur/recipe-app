# recipe_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, logout_view, logout_success_view # Project-level views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Project includes the sales app (for homepage at '')
    path('', include('sales.urls')), 

    # Project includes the recipes app (for '/recipes/')
    path('recipes/', include('recipes.urls')), 

    # Project defines the auth URLs directly
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout/success/', logout_success_view, name='logout_success'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)