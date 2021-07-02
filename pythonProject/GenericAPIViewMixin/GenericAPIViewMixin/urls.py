
from django.contrib import admin
from django.urls import path
from GenericAPIViewMixinApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('StudentApi/', views.StudentList.as_view()),
    #path('StudentApi/', views.StudentCreate.as_view()),
    #path('StudentApi/<int:pk>/', views.StudentRetrive.as_view()),
    #path('StudentApi/<int:pk>/', views.StudentUpdate.as_view()),
    path('StudentApi/<int:pk>/', views.StudentDestroy.as_view()),
]
