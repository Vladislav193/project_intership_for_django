from rest_framework import viewsets
from .serializers import CustomUserSerializer, DivisionSerializer
from .models import User, Division


class UsersViewSet(viewsets.ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = CustomUserSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer