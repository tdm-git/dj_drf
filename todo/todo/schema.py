import graphene
from graphene_django import DjangoObjectType
from tasks.models import Projects, ToDo
from users.models import User


class ProjectType(DjangoObjectType):
    class Meta:
        model = Projects
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    all_todos = graphene.List(ToDoType)
    all_users = graphene.List(UserType)

    def resolve_all_projects(root, info):
        return Projects.objects.all()

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_project_by_id(self, info, id):
        try:
            return Projects.objects.get(id=id)
        except Projects.DoesNotExist:
            return None


class ToDoMutation(graphene.Mutation):
    class Arguments:
        description = graphene.String(required=True)
        id = graphene.ID()

    todo = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, description, id):
        todo = ToDo.objects.get(pk=id)
        todo.description = description
        todo.save()
        return ToDoMutation(todo=todo)


class ToDoDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    todo = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info,  id):
        todo = ToDo.objects.get(pk=id)
        todo.delete()
        return ToDoMutation(todo=todo)

class Mutation(graphene.ObjectType):
    update_todo = ToDoMutation.Field()
    delete_todo = ToDoDelete.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)