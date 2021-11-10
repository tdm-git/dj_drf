from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import User
from .serializers import UsersModelSerializer
from rest_framework import mixins


class UsersCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UsersModelSerializer
