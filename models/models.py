from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Categories(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Locations(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Reviews(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Ratings(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Company(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    website = models.CharField(max_length=30)
    emailField = models.EmailField(max_length=30)
    phone = models.TextField(max_length=30)
    address = models.TextField(max_length=30)
    categories = models.TextField(max_length=30)
    rating = models.TextField(max_length=30)
    reviews = models.TextField(max_length=30)
    photos = models.TextField(max_length=30)

