from django.conf.urls import include, url
from rest_framework import routers

from head.views import index, react, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', ProfileViewSet)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^react$', react, name='react'),
]
