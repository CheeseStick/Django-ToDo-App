from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoListLV.as_view(), name="ListIndex"),
    path('<int:list_id>/', views.ToDoListItemLV.as_view(), name="ListDetail"),
]