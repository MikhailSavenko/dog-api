from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import DogViewSet, BreedViewSet



router = DefaultRouter()

router.register(r"dogs", DogViewSet, basename="dog")
router.register(r"breed", BreedViewSet)


urlpatterns = [
    path("", include(router.urls))
]
