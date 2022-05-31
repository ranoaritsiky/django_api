from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Job
from .serializers import JobSerializers

class JobViewSet(ModelViewSet):
    serializer_class=JobSerializers
    def get_queryset(self):
        return Job.objects.all()