from django.db import models


# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Email=models.TextField()
    PhoneNumber=models.IntegerField()
    Dateofjoin=models.TextField()
