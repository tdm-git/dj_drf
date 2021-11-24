from django.db import models
from users.models import User


class Projects(models.Model):
    name = models.CharField(max_length=256, unique=True)
    url_git = models.URLField(blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'proj {self.pk} - {self.name}'

class ToDo(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, unique=False)
    description = models.TextField()
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    is_active = models.BooleanField()
