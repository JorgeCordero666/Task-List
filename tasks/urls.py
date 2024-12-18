from django.urls import path
from .views import list_tasks, create_task, delete_task

urlpatterns = [
    path('', list_tasks),
    path('create/', create_task),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]