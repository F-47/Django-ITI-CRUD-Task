from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='students', null=True)
    dob = models.DateField()
    courses = models.ManyToManyField(Course, through='StudentCourse')
    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.course.code}"