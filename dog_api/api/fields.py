from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class PositiveIntegerFieldFromXToY(models.PositiveIntegerField):
    """
    Кастомное поле для положительных целых чисел, которое ограничивает значение диапазоном от `x` до `y`.

    Это поле гарантирует, что значение, сохраняемое в модели, будет находиться в пределах 
    от `x` до `y` (включительно). Для этого используются валидаторы MinValueValidator и 
    MaxValueValidator.

    Атрибуты:
        x (int): Минимальное значение, которое может быть присвоено полю.
        y (int): Максимальное значение, которое может быть присвоено полю.

    Аргументы конструктора:
        x (int): Минимальное значение для поля.
        y (int): Максимальное значение для поля.

    Исключения:
        ValueError: Если `x` больше `y`, возникает исключение ValueError.
    """
    def __init__(self, x: int, y: int, *args, **kwargs):
        if x > y:
            raise ValueError(f"x ({x}) cannot be greater than y ({y})")
        kwargs['validators'] = [
            MinValueValidator(x),
            MaxValueValidator(y)
        ]
        super().__init__(*args, **kwargs)