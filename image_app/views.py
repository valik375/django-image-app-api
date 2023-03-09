from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from .models import Image
from .serializers import ImageSerializers, ImageDetailSerializers


class ImageView(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    def get_serializer_class(self):
        if self.action in ['retrieve', 'update']:
            return ImageDetailSerializers
        return ImageSerializers
    pagination_class = None
    queryset = Image.objects.all()
    permission_classes = (IsAuthenticated,)
