
from django.contrib import admin
from django.urls import path

from DRFApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.postdata),
]
