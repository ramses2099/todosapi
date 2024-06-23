from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    """
    Todo class model
    """
    # title
    title = models.CharField(max_length=600)
    #description
    description = models.CharField(max_length=600)    
    # "userId": 1,
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # completed
    completed = models.BooleanField(default=False)
    # created
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title