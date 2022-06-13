from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.TextField(null=True)
    #Author = models.ForeignKey(get_user_model())
    Author=models.ForeignKey('Post', on_delete=models.PROTECT)
    Created_date=models.DateTimeField(default = datetime.now, blank = True)
    Published_date=models.DateTimeField(default = datetime.now, blank = True)










