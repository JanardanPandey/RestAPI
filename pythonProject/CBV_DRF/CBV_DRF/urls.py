
from django.contrib import admin
from django.urls import path

from CBVapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentAPI/', views.StudentAPI.as_view()),
]
