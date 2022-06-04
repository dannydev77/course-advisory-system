from operator import mod
from random import choices
from django.db import models
from django.contrib.auth.models import User


# Create your models here
class School(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return str(self.name)


class Course(models.Model):
    name = models.CharField(max_length=200)
    schools = models.ManyToManyField(School)
    # advice = models.ManyToManyField('Advice')

    def __str__(self) -> str:
        return self.name


class Advice(models.Model):
    name = models.CharField(max_length=200)
    context = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Application(models.Model):
    GRADES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('other', 'other'),

    )
    name = models.ForeignKey(User, related_name='application', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='applications', on_delete=models.CASCADE)
    grade = models.CharField(max_length=5, null=True, blank=True, choices=GRADES)

    def __str__(self) -> str:
        return str(self.name)
