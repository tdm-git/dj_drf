from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UsersModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email')