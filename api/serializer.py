from rest_framework import serializers
from .models import Sample


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('pk', 'name', 'score',)
        extra_kwargs = {}
