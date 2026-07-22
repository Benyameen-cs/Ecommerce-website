from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(req):
    return render(req , 'accounts/login.html' , {'data' : 'data'})

def register(req):
    return render(req , 'accounts/register.html' , {'data' : 'data'})


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




