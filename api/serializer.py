from rest_framework import serializers
from .models import Sample


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ()
        extra_kwargs = {}
