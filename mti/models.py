from django.db import models

from .fields import CuidField


class Person(models.Model):
    ID = CuidField()
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Student(Person):
    school = models.CharField(max_length=32)

class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    average = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Reportcard for {self.student.name} with average {self.average}"


class Human(models.Model):
    ID = CuidField()
    name = models.CharField(max_length=64)

    class Meta:
        abstract = True


class Developer(Human):
    company = models.CharField(max_length=32)

class LinesOfCode(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    average = models.PositiveSmallIntegerField()


