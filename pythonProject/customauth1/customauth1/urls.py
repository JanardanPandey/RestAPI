from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from CustomAuthApp import views
from CustomAuthApp.customauth import CustomAuthToken

router = DefaultRouter()

router.register('studentapi', views.StudentApi , basename='StudentApi')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('gettoken/',CustomAuthToken.as_view())
]
