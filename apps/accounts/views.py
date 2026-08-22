from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import RegistrationForm , LoginForm
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate , login as auth_login

# Create your views here.

def register(req):

    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user=user
            )
            messages.success(req, 'User register successfully..')
            return redirect('login')
    else:
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




