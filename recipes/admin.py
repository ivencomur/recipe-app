from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "cook_time_minutes", "created_at")
    search_fields = ("name", "description")
    inlines = [RecipeIngredientInline]

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("recipe", "ingredient", "quantity", "unit")
    list_select_related = ("recipe", "ingredient")
