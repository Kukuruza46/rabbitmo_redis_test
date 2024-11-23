from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.age} лет, {self.gender})"
