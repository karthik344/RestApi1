from django.conf.urls import url
from .views import StatusAPIView ,StatusAPIDetailView

urlpatterns=[
    url(r'^$',StatusAPIView.as_view()),
    #url(r'^create/$',StatusCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/$',StatusAPIDetailView.as_view()),
   # url(r'^(?P<id>\d+)/update/$',StatusUpdateAPIView.as_view()),
    #url(r'^(?P<id>\d+)/delete/$',StatusDeleteAPIView.as_view()),
]




