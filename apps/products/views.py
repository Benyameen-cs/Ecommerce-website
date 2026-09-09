from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product , Category
from decimal import Decimal , InvalidOperation
from django.contrib import messages
# Create your views here.


def product_list(req):

    search_query = req.GET.get('q' , '').strip()
    category = req.GET.get('category', '').strip()
    min_price = req.GET.get('min_price' , '').strip()
    max_price = req.GET.get('max_price' , '').strip()

    products = Product.objects.all()
    categories = Category.objects.all()
    
    min_price_value = None 
    max_price_value = None 

    if min_price:
        try:
            min_price_value = Decimal(min_price)
            if min_price_value < 0:
                min_price_value = None
                messages.error(req , 'Minimum price cannot be negative')
        except InvalidOperation:
            messages.error(req,'Invlaid minimum price...')
    if max_price:
        try:
            max_price_value = Decimal(max_price)
            if max_price_value < 0:
                max_price_value = None
                messages.error(req , 'Maximum price cannot be negative..')
        except InvalidOperation:
            messages.error(req ,'Invalid maximum price..')

    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    if category:
        products = products.filter(category__name__iexact = category )

     
    invalid_price_range = False

    if min_price_value is not None and max_price_value is not None and min_price_value> max_price_value:
            messages.error(req , 'minimum price cannot be greater than miximum..')
            invalid_price_range =True
    if not invalid_price_range:
        if min_price_value is not None:
            products = products.filter(price__gte = min_price_value)
        if max_price_value is not None:
            products = products.filter(price__lte = max_price_value)

    query_params = req.GET.copy()
    query_params.pop('page', None)

    paginator = Paginator(products, 9)
    page_number = req.GET.get('page')
    page_products = paginator.get_page(page_number)

    

    context  = {
        "products" : page_products,
        'categories': categories,

        'search_query' : search_query,
        'category' : category,
        'min_price' : min_price ,
        'max_price' : max_price,
        'query_params' : query_params.urlencode(),
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
    paginator = Paginator(products , 9)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category' : category,
        'products' : page_obj
    }
    return render(req , 'products/category_details.html' , context)

def files(req  , file_path):
    return HttpResponse(f"File are located in {file_path}")