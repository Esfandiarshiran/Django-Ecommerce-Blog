# Generated by Django 4.1 on 2022-08-14 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecommerce_products', '0015_product_is_free_product_zip_file'),
        ('Ecommerce_order', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='buy_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Discount'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='stripe_payment_intent',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce_products.product'),
        ),
    ]
