from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Ecommerce_products.models import WishList, Product


@login_required(login_url='/login')
def add_to_wishlist(request, product_id=None, user_id=None):

    if not product_id and not user_id:
        user_id_in_wishlist = request.user.id
        wish_list = WishList.objects.all().filter(user_id= user_id_in_wishlist)
        products = Product.objects.all().filter(wishlist__user_id= user_id_in_wishlist)
        user_name = request.user
        context = {
            'products': products,
            'user_name': user_name,
        }
        return render(request, 'Ecommerce_User_Dashboard/wish_list.html',context)

    message = ""
    new_wish = None
    # print(request.path)
    user = User.objects.get(id = user_id)
    product = Product.objects.get(id=product_id)
    wish_list = WishList.objects.filter(user_id=user_id, product_id=product_id)
    if wish_list.first() is None:
        new_wish = WishList(user= user, product= product)
        new_wish.save()
        message = "I has been added to your wish list successfully."
    else:
        message = 'The product is already exist in your wish list.'
    context = {
        'message':message,
    }
    context= {
        'message': message,
    }
    return render(request, 'Ecommerce_products/product_list.html',context)




# @login_required(login_url='/login')
# def remove_order_item(request, *args, **kwargs):
#     item_id = kwargs.get('item_id')
#     if item_id is not None:
#         item = CartItem.objects.get_queryset().get(id=item_id, cart__owner_id=request.user.id)
#         if item is not None:
#             item.delete()
#             return redirect('/shopping_cart')
#     raise Http404()