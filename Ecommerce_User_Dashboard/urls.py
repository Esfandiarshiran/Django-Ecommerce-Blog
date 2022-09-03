from django.urls import path
from .views import dashboard, add_to_wishlist, remove_wishlist_item, \
    add_wish_list_to_cart, profile, order_list

urlpatterns = [

    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('wish-list/', add_to_wishlist, name='wishlist'),
    path('products/add-to-wishlist/<int:product_id>/<int:user_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wish-list/add/<int:product_id>/<int:user_id>/', add_wish_list_to_cart, name='add_wish_item_to_cart'),
    path('wish-list/add/all/<int:user_id>/<str:True>/', add_wish_list_to_cart, name='add_all_wish_items_to_cart'),
    path('wish-list/delete/<int:product_id>/<int:user_id>/', remove_wishlist_item, name='delete_wishlist'),
    path('wish-list/delete/all/<int:user_id>/<str:True>/', remove_wishlist_item, name='delete_all_wishlist'),
    path('order-list/<int:user_id>/', order_list, name='delete_all_wishlist'),

]
