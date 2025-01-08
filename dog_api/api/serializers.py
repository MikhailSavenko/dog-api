from rest_framework import serializers

from breed.models import Breed
from dog.models import Dog


class DogSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Dog.

    Поля:
        Смотри описание полей в модели Dog.

    Дополнительные поля:
        breed_average_age (FloatField): Средний возраст собак той же породы.
            Поле только для чтения, берётся из аннотации 'avg_age_breed'.
        same_breed_count (IntegerField): Количество собак той же породы.
            Поле только для чтения, берётся из аннотации 'count_dog'.

    Класс Meta:
        model (Dog): Модель Dog, используемая для сериализации.
        fields (str): Включает все поля модели.
    """

    breed_average_age = serializers.FloatField(read_only=True, source="avg_age_breed")
    same_breed_count = serializers.IntegerField(read_only=True, source="count_dog")

    class Meta:
        model = Dog
        fields = "__all__"


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Breed.

    Поля:
        Смотри описание полей в модели Breed.

    Дополнительные поля:
        count_dogs (IntegerField): Количество собак этой породы.
            Поле только для чтения, берётся из аннотации 'avg_age_breed'

    Класс Meta:
        model (Breed): Модель Breed, используемая для сериализации.
        fields (str): Включает все поля модели.
    """

    count_dogs = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = "__all__"
