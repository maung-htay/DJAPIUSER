from django.urls import path, include
from .apiviews import CountryList, CountryDetail, AddressList, AddressDetail, AuthorList, AuthorDetail, BookList, BookDetail


urlpatterns = [
    path("country/", CountryList.as_view(), name="country_list"),
    path("country/<int:pk>/", CountryDetail.as_view(), name="country_detail"),

    path("address/", AddressList.as_view(), name="address_list"),
    path("address/<int:pk>/", AddressDetail.as_view(), name="address_detail"),

    path("author/", AuthorList.as_view(), name="author_list"),
    path("author/<int:pk>/", AuthorDetail.as_view(), name="author_detail"),

    path("book/", BookList.as_view(), name="book_list"),
    path("book/<int:pk>/", BookDetail.as_view(), name="book_detail"),
]
