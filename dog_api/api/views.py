from rest_framework import viewsets
from dog.models import Dog
from breed.models import Breed
from api.serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer