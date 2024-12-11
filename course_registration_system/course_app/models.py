from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=100, default='')
    maximum_capacity = models.IntegerField()
    current_enrolled = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(unique=True)
    enrolled_courses = models.ManyToManyField(Course, related_name='students')


    def __str__(self):
        return self.name