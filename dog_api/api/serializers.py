from rest_framework import serializers
from dog.models import Dog
from breed.models import Breed


class DogSerializer(serializers.ModelSerializer):
    breed_average_age = serializers.FloatField(read_only=True, source="avg_age_breed")
    same_breed_count = serializers.IntegerField(read_only=True, source="count_dog")
    
    class Meta:
        model = Dog
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    count_dogs = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Breed
        fields = '__all__'