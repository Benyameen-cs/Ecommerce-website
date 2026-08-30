from django.contrib import admin
from django import forms
from .models import Order , OrderItems , ShippingAddress
# Register your models here.


class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_status(self):
        new_status = self.cleaned_data['status']
        if self.instance.pk:
            old_status = self.instance.status
            if new_status != old_status:
                if not self.instance.can_transitions_to(new_status):
                    raise forms.ValidationError(
                        'Invalid status transitions'
                        f"{old_status} -> {new_status}"
                    )
        return new_status


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

    form = OrderAdminForm

    list_display = (
        'id' ,
        'customer' ,
        'status' ,
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )
    search_fields = (
        'customer__user__username',
        'customer__user__email',
    )
    ordering = ('-created_at',)
    inlines = [OrderItemsInline , ShippingAddressInline]