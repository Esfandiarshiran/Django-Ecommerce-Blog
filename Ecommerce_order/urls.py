from django.urls import path
from .views import add_item_to_cart, shopping_cart, remove_order_item, check_out


app_name = 'order'

urlpatterns = [
    path('add-item-to-cart/<int:product_id>/', add_item_to_cart, name= 'add_item_to_cart'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('remove-order-item/<item_id>/', remove_order_item, name='remove_order_item'),
    path('shopping_cart/check_out/', check_out, name= 'check_out'),
]
