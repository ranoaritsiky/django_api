from django.contrib import admin

from .models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display=['name','date_created','date_updated','description']

admin.site.register(Job,JobAdmin)