from django.db import models
from django.utils import timezone

class Todo(models.Model):
    todo_title = models.CharField(max_length=200)
    todo_description = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_title
    

# Create your models here.
