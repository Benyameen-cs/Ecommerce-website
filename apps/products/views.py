from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def product_list(req):
    
    context  = {
        "products" : [
        {
            'id' : 1,
            'type': 'pant',
            'name' : 'Watch',
            'discountPrice' : 5000,
            'originalPrice': 5500,
            'quantity' : 12,

        },
        {
            'id' : 2,
            'type': 'Electric',
            'name' : 'clock',
            'discountPrice' : 5300,
            'originalPrice': 5500,
            'quantity' : 22,
        },
        {
            'id' : 3,
            'type': 'cups',
            'name' : 'large Tea Cup set',
            'discountPrice' : 10000,
            'originalPrice': 15000,
            'quantity' : 2,
        },
        {
            'id' : 4,
            'type': 'bats',
            'name' : 'Hard ball cricket bat',
            'discountPrice' : 2000,
            'originalPrice': 2500,
            'quantity' : 1,
        },
        {
            'id' : 5,
            'type': 'pant',
            'name' : 'men pants',
            'discountPrice' : 5000,
            'originalPrice': 5500,
            'quantity' : 12,
        },
        {
            'id' : 6,
            'type': 'watch',
            'name' : 'men rado brand watch',
            'discountPrice' : 25000,
            'originalPrice': 30500,
            'quantity' : 1,
        },
        {
            'id' : 7,
            'type': 'cloth',
            'name' : 'men polo shirt',
            'discountPrice' : 5000,
            'originalPrice': 5500,
            'quantity' : 12,
        }, 
    ]
    }
    return render(req , 'products/product_list.html' , context)


def product_detail(req , id): 
    context = {
        'productId' : '12',
        'productType': 'PERFUME',
        'productName' : 'J.Perfume for men 10 x lasting' ,
        'ProductOriginalPrice' : 2500,
        'productDiscountPrice':2000,
        'productDescription': "A floral, solar and voluptuous interpretation composed by Olivier Polge, Perfumer-Creator for the House of CHANEL. its very good and very pleasant to use. and we also want to offer a great deal on this  product.+ it has a unique scent that lasts long.",
    }
    return render(req , 'products/product_detail.html' , context)




def categories(req ):
    return render(req , 'products/category.html' , { 'data': 'khan'})


def category_detail(req , name):
    return render(req , 'products/category_details.html' , { 'categoryName' : name})

def files(req  , file_path):
    return HttpResponse(f"File are located in {file_path}")