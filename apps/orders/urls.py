
from django.urls import path

from . import views 

urlpatterns = [
    path('' , views.orders , name='orders'),
    path('cart/' , views.cart , name='cart'),
    path('cart/add_to_cart/<int:product_id>/' , views.add_to_cart , name='add_to_cart'),
    path('cart/decrease/<int:product_id>/' , views.decrease_cart_item , name='decrease_cart_item'),
    path('cart/increase/<int:product_id>/' , views.increase_cart_item , name='increase_cart_item'),
    path('cart/remove_cart_item/<int:product_id>/' , views.remove_cart_item , name='remove_cart_item'),
    path('checkout/' , views.checkout , name='checkout'),
    path('checkout/success_page/' , views.success_page, name='order_success_page')
]
