# urls.py
from django.conf.urls import url, include
from picture.models import TempPictureModel
from rest_framework import routers, serializers, viewsets
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
from rest_framework import viewsets
from enumfields.drf.serializers import EnumSupportSerializerMixin
from django.contrib.auth.models import Group
from django.db.models import BooleanField, Case, Q, When
from django.utils import timezone
from django.db.models.functions import Now
from .views import TestModelViewSet, UploadModelViewSet


router = routers.DefaultRouter()
router.register(r'pictures', TestModelViewSet)
router.register(r'upload', UploadModelViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]