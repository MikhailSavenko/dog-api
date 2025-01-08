from django.db import models
from django.db.models import OuterRef, Avg, Subquery, Count


class DogQuerySet(models.QuerySet):
    def with_breed_average_age(self) -> models.QuerySet:
        sub = self.filter(breed=OuterRef("breed")).values("breed").annotate(avg_age=Avg("age")).values("avg_age")
        query = self.annotate(avg_age_breed=Subquery(sub))
        return query

    def with_same_breed_count(self):
        sub = self.filter(breed=OuterRef("breed")).values("breed").annotate(count_dog=Count("id")).values("count_dog")
        query = self.annotate(count_dog=Subquery(sub))
        return query