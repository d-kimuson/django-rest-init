from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django_filters.rest_framework import DjangoFilterBackend

from .serializer import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
