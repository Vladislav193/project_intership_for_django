from django.urls import path, include
from rest_framework import routers

from .views import UsersViewSet, DivisionViewSet

app_name = "users"

router = routers.DefaultRouter()
router.register("create", UsersViewSet, basename="user")
router.register("division", DivisionViewSet, basename="division")

urlpatterns = [
    path("users/", include(router.urls))
]
