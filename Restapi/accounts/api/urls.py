from django.conf.urls import url,include
from django.contrib import admin
from .views import AuthView,RegisterAPIView

from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [
url(r'^$',AuthView.as_view()),
url(r'^Register$',RegisterAPIView.as_view()),

url(r'^jwt/$',obtain_jwt_token),
url(r'^jwt/refresh/$',refresh_jwt_token),
    ]