from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer'
    )
    phone_no = models.CharField(max_length=15 , blank=True)
    city = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=150, blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

