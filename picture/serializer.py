from .models import TempPictureModel
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
from rest_framework import viewsets
from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework import routers, serializers, viewsets

class EnterprisePictureSerializer(EnumSupportSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TempPictureModel
        fields = ('id','title','user_id','image','thumbnail','thumbnail400','expired')

    image = HyperlinkedSorlImageField('1024')

    thumbnail = HyperlinkedSorlImageField(
        '200x200',
        options={"crop": "center"},
        source='image',
        read_only=True
    )

    thumbnail400 = HyperlinkedSorlImageField(
        '200x200',
        options={"crop": "center"},
        source='image',
        read_only=True
    )
    # A thumbnail image, sorl options and read-only


class PremiumPictureSerializer(EnumSupportSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TempPictureModel
        fields = ('id','title','user_id','image','thumbnail','expired')

    image = HyperlinkedSorlImageField('1024')
    # A thumbnail image, sorl options and read-only
    thumbnail = HyperlinkedSorlImageField(
        '200x200',
        options={"crop": "center"},
        source='image',
        read_only=True
    )
    # A thumbnail image, sorl options and read-only


class BasicPictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TempPictureModel
        fields = ('id','title','user_id','thumbnail','expired')

    # A thumbnail image, sorl options and read-only
    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True
    )
