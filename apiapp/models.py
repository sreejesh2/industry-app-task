from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=500)
    created_date=models.DateTimeField(auto_now_add=True)