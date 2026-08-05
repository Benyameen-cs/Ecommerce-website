from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phoneNo = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=150)

    def __str__(self):
        return self.name

