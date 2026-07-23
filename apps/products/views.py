from django.shortcuts import render
from django.http import HttpResponse

from .models import Product , Category
# Create your views here.


def product_list(req):
    products = Product.objects.all()
    context  = {
        "products" : products
    }
    return render(req , 'products/product_list.html' , context)


def product_detail(req , id): 

    product = Product.objects.get(id=id)

    context = {
        'product' : product
    }
    return render(req , 'products/product_detail.html' , context)




def categories(req ):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }

    return render(req , 'products/category.html' , context)


def category_detail(req , slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'category' : category,
        'products' : products
    }
    return render(req , 'products/category_details.html' , context)

def files(req  , file_path):
    return HttpResponse(f"File are located in {file_path}")