from django.contrib import admin

# Register your models here.
from .models import ItAssets

class ItAssetsAdmin(admin.ModelAdmin):
    list_display = ['id','city','name','svc','branch_code']