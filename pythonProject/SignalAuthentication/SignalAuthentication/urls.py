
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from SignalAuthenticatioinApp import views
#from rest_framework.authtoken.views import obtain_auth_token
from SignalAuthenticatioinApp.CustomAuth import CustomAuthentication

router = DefaultRouter()

router.register('studentApi', views.StudentApi , 'studentApi')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',CustomAuthentication.as_view()),

]
