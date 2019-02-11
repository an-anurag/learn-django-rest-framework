from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class SchoolModel(models.Model):
    name = models.CharField(max_length=256)
    head_master = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class StandardModel(models.Model):
    number = models.PositiveSmallIntegerField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)


class StudentModel(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveSmallIntegerField()
    standard = models.ForeignKey(StandardModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)