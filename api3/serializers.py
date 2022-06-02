from rest_framework.serializers import ModelSerializer
from .models import University

class UniversitySerializers(ModelSerializer):
    class Meta:
        model=University
        fields=['name','date_created']