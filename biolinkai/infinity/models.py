from django.db import models

# Create your models here.
class Infinity(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phoneno=models.IntegerField(null=True)

    # def __str__(self):
    #     return f"{self.firstname} {self.lastname}"