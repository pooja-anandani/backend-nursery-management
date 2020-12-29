from django.conf.urls import re_path,include,url
from . import views
from rest_framework.routers import DefaultRouter
app_name = 'nursery_app'
router=DefaultRouter()
router.register('plant-viewset',views.PlantViewSet,basename='palnt-viewset')
urlpatterns = [
    url(r'',include(router.urls))
]

