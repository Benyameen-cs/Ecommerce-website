from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product/')
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='products') 

    def __str__(self):
        return self.name