from rest_framework import serializers

from django.contrib.auth.models import User

from fileUploader.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')