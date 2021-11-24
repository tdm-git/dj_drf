from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from tasks.views import ProjectsModelViewSet, ToDoModelViewSet
from tasks.views import ProjectsModelListAPI, ToDoModelListAPI
from users.views import UsersCustomViewSet, UsersCustomListAPI

router = DefaultRouter()
router.register('users', UsersCustomViewSet, basename='users')
router.register('projects', ProjectsModelViewSet)
router.register('todo', ToDoModelViewSet)
# router.register('param', views.ArticleParamFilterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
    # path('api/<str:version>/projects/', ProjectsModelListAPI.as_view()),
    # path('api/<str:version>/todo/', ToDoModelListAPI.as_view()),
    # path('api/<str:version>/users/', UsersCustomListAPI.as_view()),

    path('api/tasks/v.1', include('tasks.urls', namespace='v.1')),
    path('api/tasks/v.2', include('tasks.urls', namespace='v.2')),
]
