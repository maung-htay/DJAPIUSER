from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Author(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    published_country = models.ManyToManyField(Country)

    def __str__(self):
        return self.title
