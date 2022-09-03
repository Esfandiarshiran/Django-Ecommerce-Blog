from django.shortcuts import render, redirect
from Ecommerce_products.models import Product, SliderPicture
from Ecommerce_setting.models import SiteSetting
from Blog.models import Post
from Ecommerce_Product_Category.models import ProductsCategory
from Ecommerce_order.models import Cart, CartItem

def home_page(request):
    most_visit_products = Product.objects.order_by('-visit_count').all()[:12]
    latest_products = Product.objects.order_by('-id').all()[:5]
    hot_product = Product.objects.filter(hotitem=True)
    slider = SliderPicture.objects.all()
    category = ProductsCategory.objects.all()[:10]
    # product_category_dic = {
    #     'category':None
    # }
    # for cat in category:
    #     products = Product.objects.all().filter(category__title= cat.title)
    #     product_category_dic[cat] = products

    # recently post
    # All published posts.
    context = {
        'hot_items': hot_product,
        'sliders': slider,
        'most_visit_products': most_visit_products,
        'latest_products': latest_products,
        'category':category,
        # 'product_category_dic': product_category_dic,
    }
    return render(request, 'homepage.html',context)


def header(request, *arg, **kwargs):
    items_count = 0
    context = {
        'site_setting' :None,
        'items_count':None,
        'items': None,
    }
    site_setting = SiteSetting.objects.first()
    if site_setting is not None:
        context['site_setting'] = site_setting
    else:
        context['site_setting'] = 'Complete Site Management'

    try:
        cart = Cart.objects.filter(owner_id=request.user.id)
        cart_items = CartItem.objects.all().filter(cart=cart[:1])
        items = CartItem.objects.filter(cart__owner_id=request.user.id)
        for cart_item in cart_items:
            items_count += cart_item.count
    except Cart.DoesNotExist:
        items_count = 0

    context['items_count'] = items_count
    context['items'] = items

    return render(request, 'shared/header.html', context)


# Header code behind (install Django render partial)
def footer(request, *arg, **kwargs):
    context = {
    }
    site_setting = SiteSetting.objects.first()
    if site_setting is not None:
        context['site_setting'] = site_setting
    else:
        context['site_setting'] = 'Complete Site Management'
    return render(request, 'shared/footer.html', context)


# recent_posts_context