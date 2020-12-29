from django.conf.urls import include, url, re_path
from orders import views
from rest_framework.routers import DefaultRouter
app_name = 'orders_app'
router = DefaultRouter()
router.register('cart-viewset', views.UserCart, basename='cart-viewset')
router.register('order-viewset', views.ViewOrder, basename='order-viewset')
urlpatterns = [
    url(r'', include(router.urls)),
    re_path(r'^v1/place-order/$', views.PlaceOrder.as_view(), name='place_order'),
]
