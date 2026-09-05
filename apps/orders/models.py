from django.db import models , transaction 
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

    ALLOWED_TRANSITIONS = {
        StatusChoices.Pending : [ StatusChoices.Processing , StatusChoices.Cancelled],
        StatusChoices.Processing : [StatusChoices.Shipped , StatusChoices.Cancelled],
        StatusChoices.Shipped : [StatusChoices.Deliverd],
        StatusChoices.Deliverd : [],
        StatusChoices.Cancelled : [],
    }

    def can_transitions_to(self , new_status):
        allowed_status = self.ALLOWED_TRANSITIONS.get(
            self.status,
            [],
        )
        return new_status in allowed_status


    @transaction.atomic
    def cancel(self):
        print("CURRENT STATUS:", self.status)
        print("CANCELLED STATUS:", self.StatusChoices.Cancelled)
        print(
        "CAN CANCEL:",
        self.can_transitions_to(self.StatusChoices.Cancelled)
    )
        if not self.can_transitions_to(self.StatusChoices.Cancelled):
            raise ValueError(
                'This order cannot be cancelled...'
            )
        for item in self.items.select_related('product'):
            product = item.product
            product.stock += item.quantity
            product.save()

        self.status = self.StatusChoices.Cancelled
        self.save()


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
    
