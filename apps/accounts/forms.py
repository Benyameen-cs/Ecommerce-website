
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Email already exists...'
            )
        return email


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError(
                'password must me atleast 8 character'
            )
        return password