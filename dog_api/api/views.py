from rest_framework import viewsets

from api.serializers import BreedSerializer, DogSerializer
from breed.managers import BreedQuerySet
from breed.models import Breed
from dog.managers import DogQuerySet
from dog.models import Dog


class DogViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Dog. Этот ViewSet предоставляет стандартные действия CRUD 
    для управления собаками.

    Доступные HTTP-методы:
        - GET: Получить список собак или конкретную собаку по ID.
        - POST: Создать новую собаку.
        - PUT: Обновить данные существующей собаки.
        - DELETE: Удалить собаку.

    Методы:
        get_queryset: Возвращает queryset собак, с дополнительными аннотациями в зависимости от действия.
            - Для списка собак (`list`) добавляется аннотация `breed_average_age` для расчёта среднего возраста собак той же породы.
            - Для получения одной собаки (`retrieve`) добавляется аннотация `same_breed_count` для подсчёта количества собак той же породы.
    """
    serializer_class = DogSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        queryset: DogQuerySet = Dog.objects.select_related("breed")

        if self.action == "list":
            return queryset.with_breed_average_age()
        
        elif self.action == 'retrieve':
            return queryset.with_same_breed_count()
        
        return queryset


class BreedViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Breed. Этот ViewSet предоставляет стандартные действия CRUD 
    для управления породами собак.

    Доступные HTTP-методы:
        - GET: Получить список пород или конкретную породу по ID.
        - POST: Создать новую породу.
        - PUT: Обновить данные существующей породы.
        - DELETE: Удалить породу.

    Методы:
        get_queryset: Возвращает queryset пород, с дополнительными аннотациями для списка пород.
            - Для списка пород (`list`) добавляется аннотация `count_dogs` для подсчёта количества собак каждой породы.
    """
    serializer_class = BreedSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        queryset: BreedQuerySet = Breed.objects.all()

        if self.action == 'list':
            return queryset.with_count_dogs()
        
        return queryset