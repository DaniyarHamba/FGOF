from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Useres(models.Model):
    CHOICES = (('t', 'teacher'),
               ('s', 'student'))

    choice = models.CharField(max_length=1, choices=CHOICES, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    course_id = models.OneToOneField(User, on_delete=models.CASCADE)


class Courses(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

