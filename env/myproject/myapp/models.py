from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=200)
    paswword=models.CharField(max_length=200)
    def __str__(self):
        return self.username
class Patient(models.Model):
    patientname=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    paswword=models.CharField(max_length=200)
    def __str__(self):
        return self.patientname
