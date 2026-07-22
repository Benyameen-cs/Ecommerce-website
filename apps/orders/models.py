from django.db import models
from ..accounts.models import Customer
from ..products.models import Product
# Create your models here.

class Order(models.Model):

    class StatusChoices(models.TextChoices):
        PENDING = 'pending' ,'Pending'
        DELIVERD ='deliverd','Deliverd'
        SHIPPED = 'shipped','Shipped'
        CANCELLED = 'cancelled','Cancelled'

    customer = models.ForeignKey(Customer , on_delete=models.CASCADE , related_name='order')
    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    total_price = models.DecimalField(max_digits=10 ,decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} -- Customer {self.customer.user.username}"


class OrderItems(models.Model):
    Order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='items')
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return f"{self.product.name} -- Order #{self.id}"


    
