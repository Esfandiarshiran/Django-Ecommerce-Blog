from django.urls import path
from .views import Productslist, test, product_detail, SearchProductsView,\
    ProductslistCategory

urlpatterns = [

    path('products/', Productslist.as_view(), name= 'products_list'),
    path('products/<productID>/<title>/', product_detail, name= 'product_detail'),
    path('products/search/', SearchProductsView.as_view(), name= 'search_products_view'),
    path('products/<category_name>/', ProductslistCategory.as_view(), name= 'products_list_category'),
    path('test/', test),

]

