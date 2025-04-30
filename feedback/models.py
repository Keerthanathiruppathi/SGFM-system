from django.db import models

class Student(models.Model):
    reg_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.reg_number

class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
