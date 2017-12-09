from django.db import models

# 리스트
class ToDoList(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

# 리스트 내 항목
class ToDoListItem(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_created=True)
    is_done = models.BooleanField(default=False)
