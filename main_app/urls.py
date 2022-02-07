from django.urls import path
from main_app import views

urlpatterns = [
    path('',views.todoList,name='all_todo_list'),
    path('update_todo/<int:pk>',views.update_todo,name='update_todo'),
    path('delete/<int:pk>',views.delete_todo,name='delete'),

]
