from django.urls import path, include
from .apiviews import CountryList, CountryDetail, AddressList, AddressDetail, AuthorList, AuthorDetail, BookList, BookDetail

from .apiviews1 import country_list, country, authors, author, books, book

urlpatterns = [
    path("country/", CountryList.as_view(), name="country_list"),
    path("country/<int:pk>/", CountryDetail.as_view(), name="country_detail"),

    path("address/", AddressList.as_view(), name="address_list"),
    path("address/<int:pk>/", AddressDetail.as_view(), name="address_detail"),

    path("author/", AuthorList.as_view(), name="author_list"),
    path("author/<int:pk>/", AuthorDetail.as_view(), name="author_detail"),

    path("book/", BookList.as_view(), name="book_list"),
    path("book/<int:pk>/", BookDetail.as_view(), name="book_detail"),

    # apiviews1 url
    path("country1/", country_list, name="country_list1"),
    path("country1/<int:id>", country, name="country1"),

    path("author1/", authors, name="author_list1"),
    path("author1/<int:id>", author, name="author1"),

    path("books1/", books, name="books1"),
    path("books1/<int:id>", book, name="book1"),
]
