from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length = 10, primary_key= True)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.code} - {self.name}"