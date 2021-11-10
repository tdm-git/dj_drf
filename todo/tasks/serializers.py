from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Projects, ToDo
# from ..users.serializers import UsersModelSerializer


class ProjectsModelSerializer(ModelSerializer):
    # users = UsersModelSerializer(many=True)

    class Meta:
        model = Projects
        fields = ('__all__')


class ToDoModelSerializer(ModelSerializer):
    # project = ProjectsModelSerializer()
    # user = UserModelSerializer()

    class Meta:
        model = ToDo
        fields = ('__all__')
