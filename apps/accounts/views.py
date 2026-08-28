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
        form = RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user=user,
                phone_no = form.cleaned_data['phone_no'],
                city = form.cleaned_data['city'],
                street = form.cleaned_data['street'],
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

    orders = req.user.customer.orders.all()
    context = {
        'user' : req.user,
        'orders': orders ,
    }
    
    return render(req , 'accounts/profile.html' , context)




