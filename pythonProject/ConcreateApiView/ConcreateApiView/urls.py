
from django.contrib import admin
from django.urls import path
from CreateApiViewApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentApi/', views.LCConcreteAPIView.as_view()),
    path('StudentApi/<int:pk>/', views.RUDConcreteAPI.as_view()),
]
