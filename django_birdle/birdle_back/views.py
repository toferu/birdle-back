from django.shortcuts import render
from rest_framework import generics
from .serializers import BirdSerializer
from .models import Bird
# Create your views here.

class BirdList(generics.ListCreateAPIView):
    queryset = Bird.objects.all().order_by('id')
    serializer_class = BirdSerializer

class BirdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bird.objects.all().order_by('id')
    serializer_class = BirdSerializer