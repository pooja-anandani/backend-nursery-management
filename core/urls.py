from django.urls import re_path
from . import views
app_name = 'core_app'
urlpatterns = [
    re_path(r'^v1/signup/$', views.UserSignup.as_view(), name='sign_up'),
    re_path(r'^v1/signin/$', views.UserSignIn.as_view(), name='sign_in'),

]
