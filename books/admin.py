from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author_name", "genre", "book_type", "price")
    search_fields = ("name", "author_name")
    list_filter = ("genre", "book_type")
