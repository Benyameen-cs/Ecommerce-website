
from ..accounts.models import Customer 
from .models import ShippingAddress
from django import forms


class CustomerForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    class Meta:
        model = Customer
        fields = ['phone_no' , 'city' ,'street']

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError(
                'Email must end with @gmail.com'
            )
        return email


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            'name', 'phone_no' , 'city' , 'street',
        ]
    