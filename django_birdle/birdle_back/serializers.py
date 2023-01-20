from rest_framework import serializers
from .models import Bird

class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        field = ('id', 'name', 'image')