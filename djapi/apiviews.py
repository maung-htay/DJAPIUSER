from rest_framework import generics, permissions
from .models import Country, Address, Author, Book
from rest_framework.views import APIView
from .serializers import CountrySerializer, AddressSerializer, AuthorSerializer, BookSerializer
from rest_framework import status
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination


class CountryList(generics.ListCreateAPIView):
    # 1. Access all data from table (all())
    # 2. bind with serializer (many=True)
    # 3. return data (Response)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


# class AuthorList(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
class AuthorList(APIView):
    def get(self, request):
        page = self.request.query_params.get('page')
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        paginator = PageNumberPagination()
        paginated_data = paginator.paginate_queryset(serializer.data, request)
        return paginator.get_paginated_response(paginated_data)
        # return Response(serializer.data)

    def post(self, request):
        address = Address.objects.get(id=request.data['address'])
        author_instance = Author(name=request.data['name'], address=address)

        author_instance.save()

        serializer = AuthorSerializer(author_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        # return Response(serializer.data)
        paginator = PageNumberPagination()
        paginated_data = paginator.paginate_queryset(serializer.data, request)
        return paginator.get_paginated_response(paginated_data)

    def post(self, request):
        author = Author.objects.get(id=request.data['author'])
        country = Country.objects.filter(
            pk__in=request.data['published_country'])
        book_instance = Book(
            title=request.data['title'], author=author)

        book_instance.save()
        book_instance.published_country.set(country)

        serializer = BookSerializer(book_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
