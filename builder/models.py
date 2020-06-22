from django.db import models

# Create your models here.
class project(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='picss')
