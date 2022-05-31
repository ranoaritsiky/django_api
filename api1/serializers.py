from rest_framework.serializers import ModelSerializer

from .models import Job

class JobSerializers(ModelSerializer):
    class Meta:
        model=Job
        fields=['id','name','date_created','date_updated','description']