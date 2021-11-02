from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Projects, ToDo
from todo.users.serializers import UserModelSerializer


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Projects
        fields = ('__all__')


class ToDoModelSerializer(ModelSerializer):
    project = ProjectsModelSerializer()
    user = UserModelSerializer()

    class Meta:
        model = ToDo
        fields = ('__all__')
