from django.contrib import admin
from .models import Address, Country, Author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)


admin.site.register(Address)
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
