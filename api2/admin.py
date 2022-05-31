from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display=['name','nif','stat','cif','date_created']

admin.site.register(Company,CompanyAdmin)