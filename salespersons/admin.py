from django.contrib import admin
from .models import Salesperson

@admin.register(Salesperson)
class SalespersonAdmin(admin.ModelAdmin):
    list_display = ("username", "name")
    search_fields = ("username", "name")
