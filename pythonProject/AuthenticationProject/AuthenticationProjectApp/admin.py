from django.contrib import admin
from .models import StudentAuthModel
# Register your models here.
@admin.register(StudentAuthModel)
class StudenAuthModel(admin.ModelAdmin):
    list_display = ['id','name','city','roll']