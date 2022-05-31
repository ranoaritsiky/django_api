from rest_framework.serializers import ModelSerializer

from .models import Company

class CompanySerializers(ModelSerializer):
    class Meta:
        model = Company
        fields=['name','nif','stat','cif','date_created']