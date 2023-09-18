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

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.address = validated_data.get("address", instance.address)
    #     instance.save()
    #     return instance


class PostAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "address"]

    def create(self, validated_data):
        author = Author.objects.create(**validated_data)
        return author

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    published_country = CountrySerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class PostBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "author", "published_country"]
        # title = serializers.CharField(max_length=100)
        # author = serializers.IntegerField()
        # published_country = serializers.ListField(child=serializers.IntegerField())

    def create(self, validated_data):
        book = Book.objects.create(
            title=validated_data['title'],
            author=validated_data['author'])
        book.published_country.set(validated_data['published_country'])
        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.published_country.set(validated_data.get(
            "published_country", instance.published_country))
        instance.save()
        return instance
