from django.db import models
from django.utils import timezone

class Todo(models.Model):
    todo_title = models.CharField(max_length=200)
    todo_description = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.todo_title
    
    class Meta:
        ordering = ['created_date']
    
    TASK_STATUS = (
        ('n', 'Not started'),
        ('s', 'Started'),
        ('c', 'Complete')
    )

    status = models.CharField(
        max_length=1,
        choices=TASK_STATUS,
        blank=True,
        default='n',
        help_text='Task status',
    )


# Create your models here.
