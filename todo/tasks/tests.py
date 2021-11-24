import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from .views import ProjectsModelViewSet, ToDoModelViewSet
from .models import Projects, ToDo
from users.models import User


class TestProjectViewSet(TestCase):
    url = '/api/projects/'

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ProjectsModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, {'name': 'Проект № 1'})
        view = ProjectsModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, {'name': 'Проект № 1', 'users': ['1']}, format='json')
        admin = User.objects.create_superuser('test_admin', 'admin@admin.com', '123456')
        force_authenticate(request, admin)
        view = ProjectsModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        project = Projects.objects.create(name='Проект № 1')
        client = APIClient()
        response = client.get(f'{self.url}{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        project = Projects.objects.create(name='Проект № 1')
        client = APIClient()
        response = client.put(f'{self.url}{project.id}/',  {'name': 'Проект № 1', 'users': ['1']})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        project = Projects.objects.create(name='Проект № 1', url_git='https://docs.google.com/document/')
        client = APIClient()
        admin = User.objects.create_superuser('test_admin', 'admin@admin.com', 'admin123456')
        client.login(username='test_admin', password='admin123456')
        response = client.put(f'{self.url}{project.id}/', {'name': 'Проект № 1', 'url_git': 'https://docs.google.com/document/', 'users': ['1']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Projects.objects.get(id=project.id)
        self.assertEqual(project.name, 'Проект № 1')
        self.assertEqual(project.url_git, 'https://docs.google.com/document/')
        client.logout()


class TestToDoViewSet(APITestCase):
    url = '/api/todo/'

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        admin = User.objects.create_superuser('test_admin', 'admin@admin.com', 'admin123456')
        project = Projects.objects.create(name='Проект № 1', url_git='https://docs.google.com/document/')
        todo = ToDo.objects.create(description='Выполнить работу', project=project, user=admin, is_active=True)
        self.client.login(username='test_admin', password='admin123456')

        response = self.client.put(f'{self.url}{todo.id}/', {'description': 'Выполнить проект',
                        'project': project.id, 'user': admin.id , 'is_active': 'False'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = ToDo.objects.get(id=todo.id)
        self.assertEqual(todo.description, 'Выполнить проект')
        self.assertEqual(todo.is_active, False)

    def test_edit_mixer(self):
        project = mixer.blend(Projects)
        todo = mixer.blend(ToDo, project=project)
        admin = User.objects.create_superuser('test_admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='test_admin', password='admin123456')
        response = self.client.put(f'{self.url}{todo.id}/', {'description': 'Выполнить проект',
                                 'project': project.id, 'user': admin.id, 'is_active': 'False'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = ToDo.objects.get(id=todo.id)
        self.assertEqual(todo.description, 'Выполнить проект')
        self.assertEqual(todo.is_active, False)