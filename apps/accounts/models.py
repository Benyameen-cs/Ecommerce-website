from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    phoneNo = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    street = models.TextField()
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='user')

    def __str__(self):
        return self.user.username

