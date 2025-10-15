from django.db import models
from django.core.validators import MinValueValidator
from django.shortcuts import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    cook_time_minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Total cooking time in minutes",
    )
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    # Many-to-many via a join model so we can store quantity and unit
    ingredients = models.ManyToManyField(
        "Ingredient", through="RecipeIngredient", related_name="recipes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    unit = models.CharField(max_length=32, blank=True)

    class Meta:
        unique_together = ("recipe", "ingredient")