from rest_framework.viewsets import ModelViewSet

from .serializers import CompanySerializers
from .models import Company

from django.shortcuts import render

class CompanyViewSets(ModelViewSet):
    serializer_class=CompanySerializers
    def get_queryset(self):
        return Company.objects.all()