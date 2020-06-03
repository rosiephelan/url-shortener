from .models import urls
from rest_framework import serializers

class urlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = urls
        fields = ['id', 'long_url', 'short_url']