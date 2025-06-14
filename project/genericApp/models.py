from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
