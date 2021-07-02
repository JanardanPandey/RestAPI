from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class StudenAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','roll']