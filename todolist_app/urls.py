from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.todolist, name='todolist'), 
    path('delete/<task_id>', views.deleteTask, name='deleteTask'), #here "<task_id>" can be any name but must be mentioned under "<>" bracket
    path('edit/<task_id>', views.editTask, name='editTask'),
    path('complete/<task_id>', views.completeTask, name='completeTask'),
    path('pending/<task_id>', views.pendingTask, name='pendingTask'),
]