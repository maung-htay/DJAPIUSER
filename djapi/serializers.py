from rest_framework import serializers
from .models import Country, Address, Author, Book


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    published_country = CountrySerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
