from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import User
from .serializers import UsersModelSerializer, UsersModelSerializerFull
from rest_framework import mixins


# class UsersCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
class UsersCustomListAPI(ListAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v.2':
            return UsersModelSerializerFull
        return UsersModelSerializer


class UsersCustomViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UsersModelSerializer


