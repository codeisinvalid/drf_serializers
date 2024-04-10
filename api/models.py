from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    grade = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)