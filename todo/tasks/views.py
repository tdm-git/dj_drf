from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Projects, ToDo
from .serializers import ProjectsModelSerializer, ToDoModelSerializer


class ProjectsModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer


class ToDoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
