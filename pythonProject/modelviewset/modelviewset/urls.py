
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modelviewsetApp import views
from rest_framework import viewsets

router = DefaultRouter()
router.register('studentapi',views.StudentViewsets, basename='StudentAPI')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
