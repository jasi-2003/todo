from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Taskmodel(models.Model):

    task_name = models.CharField(max_length=60)

    created_date = models.DateField(auto_now_add=True)

    is_completed = models.BooleanField(default=False)

    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)



