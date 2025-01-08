from django.db import models
from django.db.models import Avg, Count, OuterRef, Subquery


class DogQuerySet(models.QuerySet):
    """
    Пользовательский QuerySet для модели Dog с дополнительными аннотациями.
    """

    def with_breed_average_age(self) -> "DogQuerySet":
        """
        Аннотирует каждую запись собаки средним возрастом собак той же породы.

        Returns:
            DogQuerySet: QuerySet с аннотацией 'avg_age_breed', представляющей
            средний возраст собак для каждой породы.
        """
        sub = self.filter(breed=OuterRef("breed")).values("breed").annotate(avg_age=Avg("age")).values("avg_age")
        query = self.annotate(avg_age_breed=Subquery(sub))
        return query

    def with_same_breed_count(self) -> "DogQuerySet":
        """
        Аннотирует каждую запись собаки количеством собак той же породы.

        Returns:
            DogQuerySet: QuerySet с аннотацией 'count_dog', представляющей
            количество собак для каждой породы.
        """
        sub = self.filter(breed=OuterRef("breed")).values("breed").annotate(count_dog=Count("id")).values("count_dog")
        query = self.annotate(count_dog=Subquery(sub))
        return query
