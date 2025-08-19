# books/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# books/serializers.py
def validate_price(self, value):
    if value <= 0:
        raise serializers.ValidationError("Narx musbat bo‘lishi kerak.")
    return value
