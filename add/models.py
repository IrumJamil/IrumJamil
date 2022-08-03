from django.db import models

# Create your models here.
class Stu(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=30)