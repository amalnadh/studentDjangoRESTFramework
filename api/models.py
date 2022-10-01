from django.db import models
  
class Student(models.Model):

    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField()
    course=models.CharField(max_length=150)
  
    def __str__(self) -> str:
        return self.name