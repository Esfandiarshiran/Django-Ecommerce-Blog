from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Blog.models import Post
from Ecommerce_order.models import Cart, OrderItem
from .models import NewsModel, WishList, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Ecommerce_products.models import Product
from .forms import ProfileForm
from django.contrib import  messages


@login_required()
def dashboard(request):
    recent_posts = Post.published.all().order_by('-create_date')[:3]
    recent_news = NewsModel.objects.all().order_by('-date')[:3]

    context = {
        'recent_posts': recent_posts,
        'recent_news': recent_news,
    }
    return render(request, 'Ecommerce_User_Dashboard/dashboard.html', context)


@login_required(login_url='/login')
def add_to_wishlist(request, product_id=None, user_id=None):
    user_id_in_wishlist = request.user.id
    if not product_id and not user_id:
        wish_list = WishList.objects.all().filter(user_id=user_id_in_wishlist)
        products = Product.objects.all().filter(wishlist__user_id=user_id_in_wishlist)
        user_name = request.user
        context = {
            'products': products,
            'user_name': user_name,
            'user_id_in_wishlist': user_id_in_wishlist,
        }
        return render(request, 'Ecommerce_User_Dashboard/wish_list.html', context)

    # message = ""
    new_wish = None
    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    wish_list = WishList.objects.filter(user_id=user_id_in_wishlist, product_id=product_id)
    if wish_list.first() is None:
        new_wish = WishList(user=user, product=product)
        new_wish.save()
        message = "I has been added to your wish list successfully."
    else:
        message = 'The product is already exist in your wish list.'
    context = {
        'message': message,
    }
    context = {

        'message': message,
    }
    # return render(request, 'Ecommerce_products/product_list.html', context)
    return redirect('/products/')


@login_required(login_url='/login')
def remove_wishlist_item(request, *args, **kwargs):
    product_id = kwargs.get('product_id')
    user_id = kwargs.get('user_id')
    delet_all = kwargs.get('True')
    if delet_all == 'True':
        new_wish = WishList.objects.filter(user_id=request.user.id)
        if new_wish is not None:
            new_wish.delete()
            return redirect('/dashboard/wish-list/')
    if user_id is not None and product_id is not None:
        new_wish = WishList.objects.filter(user_id=request.user.id, product_id=product_id).first()
        if new_wish is not None:
            new_wish.delete()
    return redirect('/dashboard/wish-list/')
    # raise Http404()


@login_required(login_url='/login')
def add_wish_list_to_cart(request, *args, **kwargs):
    product_id = kwargs.get('product_id')
    # user_id = kwargs.get('user_id')
    add_all = kwargs.get('True')
    cart = Cart.objects.filter(owner_id=request.user.id, get_paid=False).first()
    if cart is None:
        cart = Cart.objects.create(owner_id=request.user.id, get_paid=False)
    if add_all == 'True':
        wish_list = WishList.objects.all().filter(user_id=request.user.id)
        for item in wish_list:
            product_obj = Product.objects.get_by_Id(product_id=item.product_id)
            cart.cartitem_set.create(product_id=product_obj.id, price=product_obj.price, count=1)
        new_wish = WishList.objects.filter(user_id=request.user.id)
        if new_wish is not None:
            new_wish.delete()
        return redirect('/shopping_cart')
    product = Product.objects.get_by_Id(product_id=product_id)
    cart.cartitem_set.create(product_id=product.id, price=product.price, count=1)
    new_wish = WishList.objects.filter(user_id=request.user.id, product_id=product_id).first()
    if new_wish is not None:
        new_wish.delete()
    return redirect('/shopping_cart')


@login_required(login_url='/login')
def profile(request):
    user_request_id = request.user.id
    user_object = User.objects.get(id=user_request_id)
    user_profile = UserProfile.objects.filter(user=user_request_id).first()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            if user_profile and request.FILES:
                if user_profile.profile_picture in request.FILES:
                    user_profile.profile_picture = request.FILES['profile_picture']
            new_user_profile = profile_form.save(commit=False)
            user_object.email = profile_form.cleaned_data['email']
            user_object.first_name = profile_form.cleaned_data['first_name']
            user_object.last_name = profile_form.cleaned_data['last_name']
            user_object.save()
            new_user_profile.user = user_object
            new_user_profile.save()
            messages.success(request, 'Your profile has been updated successfully')
        else:
            messages.error(request, 'Profile updating failed, try it again!')
        return redirect('/dashboard')
    else:
        profile_form = ProfileForm(instance=user_profile)
    context = {
        'form': profile_form,
    }
    return render(request, 'Ecommerce_User_Dashboard/profile.html', context)


@login_required(login_url='/login')
def order_list(request, user_id):
    order_product_id = {}
    # user = User.objects.filter(id=request.user.id)
    orders = OrderItem.objects.all().filter(user_id=user_id)

    for product_id_in_orderitem in orders:
        order_product_id[product_id_in_orderitem.product.id] = 1
    products = Product.objects.all().filter(id__in=order_product_id)

    i = 0
    orders_products = {}
    for order in orders:
        orders_products[order] = products[i]
        i += 1

    orders_products = dict(reversed(list(orders_products.items())))
    context = {
        'orders': orders_products,
    }

    return render(request, 'Ecommerce_User_Dashboard/order_list.html', context)
