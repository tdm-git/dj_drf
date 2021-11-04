from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UsersModelSerializer
