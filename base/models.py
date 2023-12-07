from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.title