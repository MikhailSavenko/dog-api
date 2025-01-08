from django.db import models
from django.db.models import OuterRef, Avg, Subquery, Count


class DogQuerySet(models.QuerySet):
    def breed_average_age(self) -> models.QuerySet:
        sub = self.objects.filter(breed=OuterRef("breed")).values("breed").annotate(avg_age=Avg("age")).values("avg_age")
        query = self.objects.annotate(avg_age_breed=Subquery(sub))
        return query

    def same_breed_count(self):
        sub = self.objects.filter(breed=OuterRef("breed")).values("breed").annotate(count_dog=Count("id")).values("count_dog")
        query = self.objects.annotate(count_dog=Subquery(sub))
        return query