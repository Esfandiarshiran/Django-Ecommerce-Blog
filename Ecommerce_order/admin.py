from django.contrib import admin


# Register your models here.
from Ecommerce_order.models import Cart, CartItem, Order, OrderItem

# admin.site.register([Cart, CartItem,Order, OrderItem])
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('total', 'emailAddress', 'created')
    list_filter = ('total', 'emailAddress', 'created')
    search_fields = ('total', 'emailAddress', 'created')
    ordering = ('total', 'emailAddress', 'created')
    date_hierarchy = 'created'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'discount', 'buy_date')
    list_filter = ('product', 'price', 'discount', 'buy_date')
    search_fields = ('product', 'price', 'discount', 'buy_date')
    ordering = ('product', 'price', 'discount', 'buy_date')
    date_hierarchy = 'buy_date'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('owner', 'payment_date')
    list_filter = ('owner', 'payment_date')
    search_fields = ('owner', 'payment_date')
    ordering = ('owner', 'payment_date')
    date_hierarchy = 'payment_date'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'count', 'active')
    list_filter = ('product', 'price', 'count', 'active')
    search_fields = ('product', 'price', 'count', 'active')
    ordering = ('product', 'price', 'count', 'active')
