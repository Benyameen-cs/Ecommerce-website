from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def orders(req):
    context = {
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
    return render(req , 'orders/orders.html' , context)


def cart(req):
    context = {
        'cartItems' : [
            {
                'itemName' : 'Watch',
                'itemQuantity': 2,
                'itemPrice' : 2333,
            },
            {
                'itemName' : 'Watch',
                'itemQuantity': 2,
                'itemPrice' : 2333,
            },
            {
                'itemName' : 'Watch',
                'itemQuantity': 2,
                'itemPrice' : 2333,
            },
            {
                'itemName' : 'Watch',
                'itemQuantity': 2,
                'itemPrice' : 2333,
            },
        ]
    }
    
    return render(req , 'orders/cart.html' , context)


def checkout(req):
    return render(req , 'orders/checkout.html' , {'data': 'data'})
    

