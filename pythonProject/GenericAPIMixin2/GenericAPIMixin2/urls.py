from django.contrib import admin
from django.urls import path
from GenericAPIMixin2App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentApi/', views.StudentMixin.as_view()),
    path('StudentApi/<int:pk>/', views.StudentMixinPK.as_view()),
]
