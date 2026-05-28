from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher,
                                on_delete=models.CASCADE,
                                related_name='teacher_student',
                                null=True)
