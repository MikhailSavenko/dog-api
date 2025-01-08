from rest_framework.routers import DefaultRouter

from api.views import BreedViewSet, DogViewSet
from django.urls import include, path


router = DefaultRouter()

router.register(r"dogs", DogViewSet, basename="dog")
router.register(r"breeds", BreedViewSet, basename="breed")


urlpatterns = [
    path("", include(router.urls))
]
