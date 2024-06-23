from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

class TodoSerializer(serializers.ModelSerializer):
    """
    TodoSerializer class serializer
    """
    user = CurrentUserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Todo
        fields = '__all__'