from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import House
from .serializers import HouseSerializer

class HouseListCreateAPIView(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class HouseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
