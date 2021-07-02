from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ViewSetApp import views

router = DefaultRouter()

#register ItAssetesApi with router
router.register('ItAssetsApi',views.ItAssetsApi, basename='ITassets')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
