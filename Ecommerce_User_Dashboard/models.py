from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from Ecommerce_products.models import Product
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"profile-{instance.id}{ext}"
    return f"profile/{final_name}"


class NewsModel(models.Model):
    body = RichTextField(max_length=700)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.body


class WishList(models.Model):
    title = models.CharField(max_length=150, verbose_name="Name")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Wish list'
        verbose_name_plural = 'Wish Lists'

    def __str__(self):
        return f'{self.user.username} wish {self.product.title}'


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150,  null=True, verbose_name="First Name",
                                  default='')
    last_name = models.CharField(max_length=150,  null=True, verbose_name="Last Name", default='')
    email = models.EmailField(max_length=150, blank=False, null=False, verbose_name="email")
    mobile = models.CharField(max_length=150, blank=True, null=True, verbose_name="Mobile", default='')
    phone = models.CharField(max_length=150, blank=True, null=True, verbose_name="Mobile", default='')
    talk = models.TextField(max_length=500, blank=True, null=True, verbose_name="Talk",
                            default='Talk about yourself in one line.')
    country = models.CharField(max_length=150, blank=True, null=True, verbose_name="country", default='')
    update_date = models.DateTimeField(null=True, blank=True,default=timezone.now)
    profile_picture = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='Picture',
                                        default='/media_root/profile/70*70.png')
    birth_day = models.DateTimeField(null=True, blank=True, default='')
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('O', 'Other',),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        blank=True,
        null=True,
    )
    PROGRAMMER_CHOICES = (
        ('Y', 'Yes',),
        ('N', 'No',),
    )
    programmer = models.CharField(
        max_length=1,
        choices=PROGRAMMER_CHOICES,
        blank=True,
        null=True,
    )
