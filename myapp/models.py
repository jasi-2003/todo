from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Taskmodel(models.Model):

    task_name = models.CharField(max_length=60,null=True)

    created_date = models.DateField(auto_now_add=True,null=True)

    is_completed = models.BooleanField(default=False,null=True)

    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    priority = [
        ('high','high'),
        ('medium','medium'),
        ('low','low')
    ]

    priority_level = models.CharField(max_length=100,choices=priority,null=True)

    due_data  = models.DateTimeField(null=True)



