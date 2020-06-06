from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    gender=models.CharField(max_length=10,choices=(('M','Male'),('F','Female')))
    joinDate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name