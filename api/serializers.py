from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User




class TodoSerializer(serializers.ModelSerializer):
    """
    TodoSerializer class serializer
    """
    class Meta:
        model = Todo
        fields = '__all__'
        
class CurrentUserSerializer(serializers.ModelSerializer):
    user = TodoSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'id')