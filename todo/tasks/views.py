from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectsFilter, ToDoFilter
from .models import Projects, ToDo
from .serializers import ProjectsModelSerializer, ProjectsModelSerializerName, ToDoModelSerializer, ToDoModelSerializerName
from rest_framework.pagination import LimitOffsetPagination


class ProjectsLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectsModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Projects.objects.all()
    filterset_class = ProjectsFilter
    serializer_class = ProjectsModelSerializer


class ProjectsModelListAPI(ListAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Projects.objects.all()
    # serializer_class = ProjectsModelSerializer
    # pagination_class = ProjectsLimitOffsetPagination
    # filterset_fields  = ['name']
    filterset_class = ProjectsFilter

    def get_serializer_class(self):
        if self.request.version == 'v.2':
            return ProjectsModelSerializerName
        return ProjectsModelSerializer


class ToDoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    filterset_class = ToDoFilter
    serializer_class = ToDoModelSerializer


class ToDoModelListAPI(ListAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    # serializer_class = ToDoModelSerializer
    # pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter

    def get_serializer_class(self):
        if self.request.version == 'v.2':
            return ToDoModelSerializerName
        return ToDoModelSerializer

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()
        return Response(self.get_serializer(todo).data)

