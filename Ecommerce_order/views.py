from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404, get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone
from Ecommerce_products.models import Product
from .forms import UserNewOrderForm
from .models import Cart, CartItem, Order, OrderItem
from django.conf import settings
from django.contrib.auth.models import User
# from django.contrib import  messages
import stripe
from Ecommerce_setting.models import BankAccount

# If we don't have session for user, make one
def session_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


@login_required(login_url='/login')
def add_item_to_cart(request, product_id):

    product = Product.objects.get_by_Id(product_id=product_id)
    try:
        cart = Cart.objects.get(owner_id=request.user.id, owner_session=session_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            owner_id=request.user.id,
            owner_session=session_id(request),

        )
        cart.save()

    try:
        new_order_form = UserNewOrderForm(request.POST or None)
        if new_order_form.is_valid():
                count = new_order_form.cleaned_data.get('count')
                if count < 0:
                    count = 1
        else:
            count = 1
    except:
        return Http404('Something went wrong, Please try again.')

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, price=product.price, count=count)
        # if cart_item.count < cart_item.product.stock:
        #     cart_item.count += 1
        #     cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            price=product.price,
            count=count
        )
        cart_item.save()

    return redirect('/shopping_cart')

@login_required(login_url='/login')
def shopping_cart(request, *args, **kwargs):
    context = {
        'order': None,
        'items': None,
        'pay': 0,
        'total': 0,
        'save': 0,
        'dis_count': 0
    }
    open_order = Cart.objects.filter(owner_id=request.user.id, owner_session=session_id(request)).first()

    if open_order is not None:
        context['order'] = open_order
        context['items'] = open_order.cartitem_set.all()

        for item in open_order.get_total_price().values():
            context['total'] += item[0]
            context['pay'] += item[1]
            context['save'] += item[2]

    return render(request, 'Ecommerce_order/cart.html', context)


@login_required(login_url='/login')
def remove_order_item(request, *args, **kwargs):
    item_id = kwargs.get('item_id')
    cart = Cart.objects.get(owner_id=request.user.id, owner_session=session_id(request))
    cart_item = CartItem.objects.get(id = item_id,  cart=cart)
    cart_item.delete()
    return redirect('/shopping_cart')


@login_required(login_url='/login')
def check_out(request, *args, **kwargs):
    # todo: handel check out form
    user = User.objects.get(id= request.user.id)
    context = {
        'pay': 0,
        'total': 0,
        'save': 0,
    }
    # ---- Cart_items
    # cart = Cart.objects.get(cart__owner_id=request.user.id)
    cart_items = CartItem.objects.filter(cart__owner_id=request.user.id, active=True)
    # ---Cart
    open_order = Cart.objects.filter(owner_id=request.user.id, owner_session=session_id(request)).first()
    if open_order is not None:
        for item in open_order.get_total_price().values():
            context['total'] += item[0]
            context['pay'] += item[1]
            context['save'] += item[2]

    payment = context['pay']

    # ----------------------------------------------------------------------------------
    bank_account = BankAccount.objects.all().first()
    stripe.api_key = bank_account.secret_key  # Don't show this to user or in frontend
    stripe_total = int(payment * 100)  # (Cent * 100 ===> Dollar)
    description = bank_account.description
    data_key = bank_account.public_key
    # ------------------------------------------------------------------
    context['stripe.api_key'] = stripe.api_key
    context['stripe_total'] = stripe_total
    context['description'] = description
    context['data_key'] = data_key

    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingCity = request.POST['stripeBillingAddressCity']
            billingPostcode = request.POST['stripeBillingAddressZip']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingCity = request.POST['stripeShippingAddressCity']
            shippingPostcode = request.POST['stripeShippingAddressZip']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']
            # Make new customer on the stripe panel
            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            # charge customer with below code
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency='usd',
                description=description,
                customer=customer.id
            )

            # Creating the order

            try:
                order_details = Order.objects.create(
                    token=token,
                    total=context['pay'],
                    emailAddress=email,
                    billingName=billingName,
                    billingAddress1=billingAddress1,
                    billingCity=billingCity,
                    billingPostcode=billingPostcode,
                    billingCountry=billingCountry,
                    shippingName=shippingName,
                    shippingAddress1=shippingAddress1,
                    shippingCity=shippingCity,
                    shippingPostcode=shippingPostcode,
                    shippingCountry=shippingCountry
                )
                order_details.save()

                for cart_item in cart_items:
                    order_item = OrderItem.objects.create(
                        user=user,
                        order=order_details,
                        product=cart_item.product,
                        quantity=cart_item.count,
                        price=cart_item.product.price,
                        discount=cart_item.product.discount,
                        buy_date=timezone.now(),
                        stripe_payment_intent= "",
                    )

                    order_item.save()
                    cart_item.delete()
                    # ------- reduce stock
                    # products = Product.objects.get(id=cart_item.product.id)
                    # products.stock = int(order_item.product.stock - order_item.quantity)
                    # products.save()

                return redirect('/dashboard')
            except ObjectDoesNotExist:
                pass

        except stripe.error.CardError as e:
            return False, e

    return render(request, 'Ecommerce_order/check_out.html', context)
