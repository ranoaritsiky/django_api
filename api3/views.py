from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet

from .models import University
from .serializers import UniversitySerializers

class UniversityViewSet(ReadOnlyModelViewSet):
    serializer_class=UniversitySerializers
    def get_queryset(self):
        queryset=University.objects.all()
        university_id=self.request.GET.get('id')
        if university_id is not None:
            queryset=queryset.filter(id=university_id)
        return queryset
        # return self.queryset.filter(id=self.kwargs.get('id'))
        # return University.objects.filter(id=2)
        # queryset=University.objects.filter(id)

        # university_id=self.request.GET.get('university_id')
        # if university_id is not None:
        #     queryset= queryset.filter(university_id=university_id)
        # return queryset
        # queryset=self.queryset.filter(id=self.request.GET.get('university_id'))