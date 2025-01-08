from rest_framework import viewsets
from dog.models import Dog
from breed.models import Breed
from api.serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet): 
    serializer_class = DogSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        queryset = Dog.objects.select_related("breed")

        if self.action == "list":
            return queryset.with_breed_average_age()
        
        elif self.action == 'retrieve':
            return queryset.with_same_breed_count()
        
        return queryset


class BreedViewSet(viewsets.ModelViewSet): 
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    http_method_names = ["get", "post", "put", "delete"]