from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Ecommerce_products.models import Product


class Cart(models.Model):
    owner_session = models.CharField(max_length=400, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='Date Paid')

    class Meta:
        verbose_name = 'Shopping Cart'
        verbose_name_plural = 'Shopping Carts'

    def __str__(self):
        return self.owner.get_username()

    def get_total_price(self):
        dic = {}
        for item in self.cartitem_set.all():
            total = item.price * item.count
            each_product_dis = item.product.discount / 100
            save = each_product_dis * total
            pay = total - save
            dic[item.id] = [total, pay, save]
        return dic


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    price = models.FloatField(verbose_name='Product Price', default=0)
    count = models.IntegerField(verbose_name='Count', blank=True)
    active = models.BooleanField(default=True)

    def sub_total(self):
        return self.count * self.price

    class Meta:
        verbose_name = 'Product Detail'
        verbose_name_plural = 'Products Detail information'

    def __str__(self):
        return self.product.title


class Order(models.Model):
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Order Total')
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, blank=True)
    billingAddress1 = models.CharField(max_length=250, blank=True)
    billingCity = models.CharField(max_length=250, blank=True)
    billingPostcode = models.CharField(max_length=250, blank=True)
    billingCountry = models.CharField(max_length=250, blank=True)
    shippingName = models.CharField(max_length=250, blank=True)
    shippingAddress1 = models.CharField(max_length=250, blank=True)
    shippingCity = models.CharField(max_length=250, blank=True)
    shippingPostcode = models.CharField(max_length=250, blank=True)
    shippingCountry = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return f' Order id is :  {str(self.id)}'


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, )
    product = models.ForeignKey(Product, on_delete=models.CASCADE )
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Price')
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0)
    buy_date = models.DateTimeField(default=timezone.now)
    stripe_payment_intent = models.CharField(max_length=250, default='', blank=True, null=True)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return  f'Product  {self.product} bought by {self.user.username}'


