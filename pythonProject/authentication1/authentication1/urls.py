from django.contrib import admin
from django.urls import path, include
from authenticationAPP import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()

router.register('StudentApi',views.StudentApi , basename='studentapi' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettokken/',obtain_auth_token),
]
