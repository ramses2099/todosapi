from django.urls import path
from .views import TodoAV, TodoDetailsAV

urlpatterns = [
    path('v1/todos',TodoAV.as_view(), name='todos-list'),
    path('v1/todos/<int:pk>', TodoDetailsAV.as_view(), name='todos-list-details'),
]
