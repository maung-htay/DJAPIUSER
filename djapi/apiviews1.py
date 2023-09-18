from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Country, Address, Author, Book
from .serializers import CountrySerializer, AuthorSerializer, PostAuthorSerializer, \
    BookSerializer, PostBookSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


@api_view(['GET', 'POST'])
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def country(request, id):
    if request.method == 'GET':
        country = Country.objects.get(pk=id)
        serializer = CountrySerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        country = Country.objects.get(pk=id)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        country = get_object_or_404(Country, pk=id)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def authors(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = PostAuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.create(validated_data=serializer.validated_data)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def author(request, id):
    if request.method == 'GET':
        author = Author.objects.get(pk=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        author = Author.objects.get(pk=id)
        serializer = PostAuthorSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.update(
            instance=author, validated_data=serializer.validated_data)
        serializer = AuthorSerializer(author)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        author = get_object_or_404(Author, pk=id)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        paginator = PageNumberPagination()
        paginated_data = paginator.paginate_queryset(serializer.data, request)
        return paginator.get_paginated_response(paginated_data)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = PostBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        books = serializer.create(validated_data=serializer.validated_data)
        serializer = BookSerializer(books)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def book(request, id):
    if request.method == 'GET':
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        book = Book.objects.get(pk=id)
        serializer = PostBookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.update(
            instance=book, validated_data=serializer.validated_data)
        serializer = BookSerializer(book)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        book = get_object_or_404(Book, pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
