from django.shortcuts import render

from Ecommerce_Product_Category.models import ProductsCategory

# In this way we don't partial render, so easly we can render our data just don't forget this config in setting.
# Templates -- Context_processors --  'Ecommerce_products.context_processors.all_category_context'
from Ecommerce_order.models import Cart, CartItem
from Ecommerce_order.views import session_id


def all_category_context(request):
    all_category = ProductsCategory.objects.all()
    return dict(category_context=all_category)


def cart_items_context(request):
    items_count = 0
    dic = {}
    if 'admin' in request.path:
        return dic
    else:
        try:
            cart = Cart.objects.filter(owner_id=request.user.id)
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            items = CartItem.objects.filter(cart__owner_id=request.user.id)
            for cart_item in cart_items:
                items_count += cart_item.count
        except Cart.DoesNotExist:
            items_count = 0

        dic['items_count'] = items_count
        dic['items'] = items
    return dic
