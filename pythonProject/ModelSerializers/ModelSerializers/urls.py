
from django.contrib import admin
from django.urls import path
from  ModelSerializersApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentAPI/', views.StudentAPI.as_view()),
]
