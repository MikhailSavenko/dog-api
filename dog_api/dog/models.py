from django.db import models
from dog_api.breed.models import Breed
from django.core.validators import MinValueValidator, MaxValueValidator


class Dog(models.Model):
    """
    Represents a dog with attributes like name, age, breed, gender, color and preferences.

    Attributes:
        name (str): The name of the dog, with a maximum length of 150 characters.
        age (int): The age of the dog, a positive integer between 1 and 30 (inclusive).
        breed (Breed): The breed of the dog, linked to the Breed model.
        gender (str): The gender of the dog, with a maximum length of 150 characters.
        color (str): The color of the dog, with a maximum length of 200 characters.
        favorite_food (str): The dog's favorite food, with a maximum length of 250 characters.
        favorite_toy (str): The dog's favorite toy, with a maximum length of 250 characters.
    """
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(30)
    ])
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=150)
    color = models.CharField(max_length=200)
    favorite_food = models.CharField(max_length=250)
    favorite_toy = models.CharField(max_length=250)

