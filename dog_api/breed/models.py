from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .managers import BreedQuerySet


class Breed(models.Model):
    """
    Модель, представляющая породу собаки с атрибутами, связанными с её характеристиками.

    Атрибуты:
        name (str): Название породы, максимальная длина 200 символов.
        size (str): Размер породы, представленный как выбор из предустановленных вариантов:
            "Tiny", "Small", "Medium", "Large".
        friendliness (int): Оценка дружелюбия породы, целое число от 1 до 5.
        trainability (int): Оценка обучаемости породы, целое число от 1 до 5.
        shedding_amount (int): Оценка интенсивности линьки породы, целое число от 1 до 5.
        exercise_needs (int): Оценка потребности в физической активности породы, целое число от 1 до 5.
    """

    class SizeChoices(models.TextChoices):
        """
        Перечисление возможных размеров породы собаки.
        """

        TINY = "Tiny"
        SMALL = "Small"
        MEDIUM = "Medium"
        LARGE = "Large"

    name = models.CharField(max_length=200)
    size = models.CharField(choices=SizeChoices.choices, max_length=6, default=SizeChoices.MEDIUM)
    friendliness = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    shedding_amount = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exercise_needs = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    objects = BreedQuerySet.as_manager()
