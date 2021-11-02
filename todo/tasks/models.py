from django.db import models
from users.models import User


class Projects(models.Model):
    name = models.CharField(max_length=256, unique=True)
    url_git = models.URLField(blank=True)
    users = models.ManyToManyField(User)


class ToDo(models.Model):
    project = models.OneToOneField(Projects, on_delete=models.CASCADE)
    description = models.TextField()
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
