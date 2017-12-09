from django.views.generic import ListView
from .models import ToDoList, ToDoListItem

class ToDoListLV(ListView):
    model = ToDoList
    template_name = "todolist/todolist_list.html"
    context_object_name = 'todolist'


class ToDoListItemLV(ListView):
    model = ToDoListItem
    template_name = "todolist/todolistitem_list.html"
    context_object_name = 'todoitems'
