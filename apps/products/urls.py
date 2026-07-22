
from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.product_list , name= 'product_list'),
    path('<int:id>/' , views.product_detail , name='product_detail'),
    path('category/' , views.categories , name = 'category'),
    path('category/<slug:name>/' , views.category_detail , name= 'category_detail'),
    path('files/<path:file_path>/' , views.files , name='files')
]