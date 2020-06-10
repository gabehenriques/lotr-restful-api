from django.conf.urls import include, url
from rest_framework import routers
from lotr_v2.api import *

router = routers.DefaultRouter()


router.register(r"character", CharacterResource)


urlpatterns = [
    url(r"^api/v2/", include(router.urls)),
]
