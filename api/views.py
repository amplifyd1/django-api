from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class CreateView(generics.listCreateAPIView):
  """This class defines the creation behavior of our rest API"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
      """Saves post data when new bucketlist is created"""
      serializer.save()
# Create your views here.
