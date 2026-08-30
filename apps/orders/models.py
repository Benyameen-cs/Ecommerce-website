from django.db import models
from ..accounts.models import Customer
from ..products.models import Product
# Create your models here.

class Order(models.Model):

    class StatusChoices(models.TextChoices):
        Pending = 'Pending' ,'Pending'
        Processing = 'Processing', 'Processing' 
        Deliverd ='Deliverd','Deliverd'
        Shipped = 'Shipped','Shipped'
        Cancelled = 'Cancelled','Cancelled'

    customer = models.ForeignKey(Customer , on_delete=models.CASCADE , related_name='orders')
    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.Pending
    )
    total_price = models.DecimalField(max_digits=10 ,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItems(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='items')
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return f"{self.product.name} -- Order #{self.id}"


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name= 'shipping_address'
    )

    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=150)

    def __str__(self):
        return f"shipping address of order {self.order.id}"
    
