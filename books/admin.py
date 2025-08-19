# books/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'genre', 'published_date')  # Qaysi maydonlar ko‘rsatilishi
    search_fields = ('title', 'author', 'genre')  # Qidirish uchun maydonlar
    list_filter = ('genre', 'published_date')  # Filtrlar
