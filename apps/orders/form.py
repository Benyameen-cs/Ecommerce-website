
from ..accounts.models import Customer
from django import forms


class CustomerForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    class Meta:
        model = Customer
        fields = ['phoneNo' , 'city' ,'street']

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError(
                'Email must end with @gmail.com'
            )
        return email

    