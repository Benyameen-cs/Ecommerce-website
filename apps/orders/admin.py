from django.contrib import admin
from .models import Order , OrderItems , ShippingAddress
# Register your models here.


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0
    readonly_fields = (
        'product', 'quantity' , 'price',
    )
    can_delete = False


class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress
    extra = 0

    readonly_fields = (
        'name' , 'phone_no' , 'city' , 'street',
    )
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id' ,'customer' , 'status' , 'created_at',)
    list_filter = ('status' ,'created_at')
    search_fields = ('customer__user__username' , 'customer__user__email',)
    ordering = ('-created_at',)
    inlines = [OrderItemsInline , ShippingAddressInline]
