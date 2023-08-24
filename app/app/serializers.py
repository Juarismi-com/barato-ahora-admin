from rest_framework import serializers, viewsets, permissions
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
   email = serializers.EmailField(required=True, trim_whitespace=True)
    
   class Meta:
      model = User
      fields = ('url', 'username', 'email', 'groups',)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
