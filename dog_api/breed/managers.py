from django.db import models
from django.db.models import Count


class BreedQuerySet(models.QuerySet):
    """
    Пользовательский QuerySet для модели Breed с дополнительными аннотациями.
    """

    def with_count_dogs(self) -> "BreedQuerySet":
        """
        Аннотирует каждую запись породы количеством собак, принадлежащих к этой породе.

        Returns:
            BreedQuerySet: QuerySet с аннотацией 'count_dogs', представляющей
            количество собак для каждой породы.
        """
        query = self.annotate(count_dogs=Count("dog"))
        return query
