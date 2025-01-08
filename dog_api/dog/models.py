from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from breed.models import Breed
from .managers import DogQuerySet


class Dog(models.Model):
    """
    Представляет собаку с такими аттрибутами, как имя, возраст, порода, пол, цвет и предпочтения.

    Атрибуты:
        name (str): Имя собаки, максимальная длина 150 символов.
        age (int): Возраст собаки, положительное целое число от 1 до 30 (включительно).
        breed (Breed): Порода собаки, связана с моделью Breed.
        gender (str): Пол собаки, максимальная длина 150 символов.
        color (str): Цвет собаки, максимальная длина 200 символов.
        favorite_food (str): Любимая еда собаки, максимальная длина 250 символов.
        favorite_toy (str): Любимая игрушка собаки, максимальная длина 250 символов.
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

    objects = DogQuerySet.as_manager()
