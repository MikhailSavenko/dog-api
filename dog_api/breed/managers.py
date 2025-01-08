from django.db import models
from django.db.models import Count


class BreedQuerySet(models.QuerySet):
    def with_count_dogs(self):
        query = self.annotate(count_dogs=Count('dog'))
        return query