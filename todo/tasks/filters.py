from django_filters import rest_framework as filters
from .models import Projects, ToDo


class ProjectsFilter(filters.FilterSet):
   name = filters.CharFilter(lookup_expr='contains')

   class Meta:
       model = Projects
       fields = ['name']


class ToDoFilter(filters.FilterSet):
   project = filters.CharFilter(lookup_expr='contains')

   class Meta:
       model = ToDo
       fields = ['project']