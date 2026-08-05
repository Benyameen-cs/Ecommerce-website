
from ..accounts.models import Customer
from django import forms


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name' ,'email','phoneNo' , 'city' ,'street']

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError(
                'Email must end with @gmail.com'
            )
        return email

    