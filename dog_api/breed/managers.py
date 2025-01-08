from django.db import models
from django.db.models import OuterRef, Avg, Subquery, Count


class BreedQuerySet(models.QuerySet):
    def count_dogs(self):
        query = self.annotate(count_dogs=Count('dog'))
        return query