from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import RegistrationForm , LoginForm
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(req):

    if req.method == 'POST':
        print('register if block')
        form = RegistrationForm(req.POST)
        print('before form validation')
        if form.is_valid():
            print('After form validation')
            print('before creating user')
            user = form.save()
            print('after creating User')
            print('before creating Customer')
            Customer.objects.create(
                user=user
            )
            print('after creating Customer')

            messages.success(req, 'User register successfully..')
            return redirect('login')
    else:
        print('register else block')
        form = RegistrationForm()

    return render(req , 'accounts/register.html' , {'form' : form})


def login(req):

    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req , username=username , password=password)
            if user is not None:
                auth_login(req , user)
                messages.success(req , 'user login successful')
                return redirect('profile')
            messages.error(req , 'invalid username and password')
    else:
        form = LoginForm()

    return render(req , 'accounts/login.html' , {'form' : form})

@login_required
def logout(req):
    if req.method == 'POST':
        auth_logout(req)
        messages.success(req , 'logout successful')
        return redirect('home')

@login_required
def change_password(req):
    if req.method == 'POST':
        form = PasswordChangeForm(req.user , req.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(req , user)
            messages.success(req , 'password change successful')
            return redirect('profile')
    else:
        form = PasswordChangeForm(req.user)
    return render(req , 'accounts/change_password.html' , {'form' : form})
    

@login_required
def profile(req):
    context = {
        'user' : {
            'userName': 'ac ali',
            'Email':'abc@gmail.com',
            'firstName':'ALI',
            'lastName' : 'Khan',
            'date_joined' :'12/1/2020',
        },
        'orders':[
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
        ]
    }
    
    return render(req , 'accounts/profile.html' , context)




