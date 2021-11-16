from .serializer import BasicPictureSerializer, PremiumPictureSerializer, EnterprisePictureSerializer
from .models import TempPictureModel
from rest_framework import routers, serializers, viewsets
from django.db.models import BooleanField, Case, Q, When
from django.utils import timezone
from django.contrib.auth.models import Group

# A larger version of the image, allows writing

class TestModelViewSet(viewsets.ModelViewSet):
    queryset = TempPictureModel.objects.all()
    serializer_class = BasicPictureSerializer
    serializer_detail_premium = PremiumPictureSerializer
    serializer_class_enterprise = EnterprisePictureSerializer

    def get_serializer_class(self):
        """
        Special case to see the user full details.
        Unless user is request.user or SYS_ADMIN for user's company
        only show basic details of user.
        """
            # if current user is sys admin of the requested user's company

        if Group.objects.get(name='Basic').user_set.filter(id=self.request.user.id).exists():
            return self.serializer_class
        elif Group.objects.get(name='Premium').user_set.filter(id=self.request.user.id).exists():
            return self.serializer_detail_premium
        elif Group.objects.get(name='Enterprise').user_set.filter(id=self.request.user.id).exists():
            return self.serializer_class_enterprise    
        else:
            return self.serializer_class     

    def get_queryset(self):
        id = self.request.user.id
        queryset = TempPictureModel.objects.filter(Q(expired__gte=timezone.now()) | Q(expired = None))
        tmp = queryset.filter(user_id=id)
        print(timezone.now())
        return tmp