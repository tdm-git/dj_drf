from django.urls import path
from .views import ProjectsModelListAPI, ToDoModelListAPI

app_name = 'tasks'
urlpatterns = [
    path('', ToDoModelListAPI.as_view()),
    # path('/projects/', ProjectsModelListAPI.as_view()),
]
