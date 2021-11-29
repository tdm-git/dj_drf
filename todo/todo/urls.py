from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from tasks.views import ProjectsModelViewSet, ToDoModelViewSet
from tasks.views import ProjectsModelListAPI, ToDoModelListAPI
from users.views import UsersCustomViewSet, UsersCustomListAPI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tasks",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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

    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),

    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
