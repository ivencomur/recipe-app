from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales.urls')),
    path('recipes/', include('recipes.urls')), # <-- ADD THIS LINE
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)