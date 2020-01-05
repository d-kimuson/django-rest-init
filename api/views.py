from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django_filters.rest_framework import DjangoFilterBackend

from .models import Sample
from .serializer import SampleSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
