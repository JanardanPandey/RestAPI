from django.contrib import admin

# Register your models here.
from .models import ITAssetsModel

@admin.register(ITAssetsModel)
class ITAssetAdmin(admin.ModelAdmin):
    list_display = ['id','region','city','svc','assetsname']