from django.db import models
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class Questions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100)
    option_four = models.CharField(max_length=100)

    def __str__(self):
        return self.questions
