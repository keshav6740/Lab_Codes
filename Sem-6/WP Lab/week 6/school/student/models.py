from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    english_marks = models.IntegerField()
    physics_marks = models.IntegerField()
    chemistry_marks = models.IntegerField()

    def total_percentage(self):
        return (self.english_marks + self.physics_marks + self.chemistry_marks) / 3
