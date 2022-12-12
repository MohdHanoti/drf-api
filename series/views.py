from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import SeriesSerializer
# Create your views here.
from .models import Series


class SeriesListView(ListCreateAPIView):
    queryset=Series.objects.all()
    serializer_class= SeriesSerializer


class SeriesDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Series.objects.all()
    serializer_class= SeriesSerializer