import itertools

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from Ecommerce_order.forms import UserNewOrderForm
from .models import Product, ProductGallery
from django.http import Http404
from Ecommerce_Product_Category.models import ProductsCategory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


class Productslist(ListView):
    paginate_by = 4
    model = Product
    # IF you make directory in your template inside the App with your App name then Automatically your
    # your page and your object would be defined by following rule:
    # default template_name is ====>     Products_list.html
    # dafult context_object_name is ===>  Products_list

    ########### Second way ######## (Not recommanded)
    # main function to retrive all product.
    # Important NOAT: function name should be exactly get_queryset to restore all products

    # def get_queryset(self):
    #     return Product.objects.all()


######################################################################################

######################################################################################
def test(request):
    hot_product = Product.objects.filter(hotitem=True)
    slider = Product.objects.all()
    context = {
        'hot_items': hot_product,
        'sliders': slider,
    }
    return render(request, 'Ecommerce_products/test.html', context)


# ========================= Detail View (FBV)#######################
# def my_grouper(n, iterable):
#     args = [iter(iterable)] * n
#     return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def product_detail(request, *args, **kwargs):
    # We can get all information from urls like this:

    # in urls ==> path('products/<productID>/<title>', product_detail)

    # Finally, we can fetch every detail about this information from DB.
    product_id = kwargs['productID']

    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': product_id})

    product = Product.objects.get_by_Id(product_id)

    if product is None or not product.active:
        raise Http404('Product was not found')
    product.visit_count += 1
    product.save()

    gallery = ProductGallery.objects.filter(product_id=product_id)

    related_products = Product.objects.get_queryset().filter(category__product=product,
                                                             category__product__recommend=True).distinct()
    # related_products = Product.objects.all().filter(category__product= product, category__product__recommend= True).distinct()
    context = {
        'product': product,
        'gallery': gallery,
        # 'related_products': grouped_related_products,
        'related_products': related_products,
        'new_order_form': new_order_form,
    }
    return render(request, 'Ecommerce_products/product_detail.html', context)


#################### Product search view ######################

class SearchProductsView(ListView):
    paginate_by = 4
    model = Product

    # For filtering and other essential search operations first we have to customize our data ,and then send to template
    def get_queryset(self):
        request = self.request
        query = request.GET.get('search')
        if query is not None:
            # return Product.objects.filter(title__icontains=query, active=True)
            return Product.objects.search(query)
        return Product.objects.get_active_products()


class ProductslistCategory(ListView):
    template_name = 'Ecommerce_products/product_list.html'
    paginate_by = 4

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductsCategory.objects.filter(title__iexact=category_name).first()
        if category is None:
            raise Http404('Page was not Found')

        return Product.objects.get_product_by_category(category_name)


