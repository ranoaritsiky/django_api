from django.contrib import admin
from .models import University
# Register your models here.

class UniversityAdmin(admin.ModelAdmin):
    list_display=['id','name','date_created']

admin.site.register(University,UniversityAdmin)