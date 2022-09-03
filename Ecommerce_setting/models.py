import os

from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_logo_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"logo/{final_name}"


class SiteSetting(models.Model):
    title = models.CharField(max_length=150, verbose_name='Site Title', default="Your Title in Site Management")
    address = models.CharField(max_length=400, verbose_name='Address', blank=True,
                               default="Your Address in Site Management")
    first_phone = models.CharField(max_length=50, verbose_name='First Phone Number', blank=True, default="09366449567")
    second_phone = models.CharField(max_length=50, verbose_name='Second Phone Number', blank=True,
                                    default="second phone number")
    third_phone = models.CharField(max_length=50, verbose_name='Third Phone Number', blank=True,
                                   default='Third Phone Number')
    first_mobile = models.CharField(max_length=50, verbose_name='First Mobile Number', blank=True,
                                    default='09366449561')
    second_mobile = models.CharField(max_length=50, verbose_name='Second Mobile Number', blank=True,
                                     default='Second Mobile Number')
    third_mobile = models.CharField(max_length=50, verbose_name='Third Mobile Number', blank=True,
                                    default='Third Mobile Number')
    fax = models.CharField(max_length=50, verbose_name='Fax', blank=True, default='Fax number Number')
    first_email = models.EmailField(max_length=50, verbose_name='First Email Address', blank=True,
                                    default='esf.shiran@gmail.com')
    second_email = models.EmailField(max_length=50, verbose_name='Second Email Address', blank=True,
                                     default='SecondEmail@email.com')
    third_email = models.EmailField(max_length=50, verbose_name='Third Email Address', blank=True,
                                    default='ThirsEmail@email.com')
    introduce = models.TextField(verbose_name='Who you are ?', null=True, blank=True, max_length=400,
                                 default='write in Site Management who you ar ! (Small summery for footer and about us page)')
    description = RichTextField(max_length=30000, verbose_name='Full descriptions',
                                default="Write Full Description in SiteManegmante for About us page")
    copy_right = models.CharField(verbose_name='Copyright', null=True, blank=True, max_length=150,
                                  default='write your Copyright in site management')
    facebook = models.URLField(verbose_name='FaceBook Link', blank=True, default='www.facebook.com')
    twitter = models.URLField(verbose_name='Twitter Link', blank=True, default='www.twitter.com')
    instagram = models.URLField(verbose_name='Instagram', blank=True, default='www.instagram.com')
    header_logo = models.ImageField(upload_to=upload_logo_image_path, null=True, blank=True,
                                    verbose_name='Logo in header', default='/media_root/logo/black_logo.png')
    footer_logo = models.ImageField(upload_to=upload_logo_image_path, null=True, blank=True,
                                    verbose_name='Logo in footer', default='/media_root/logo/white_logo.png')
    terms_of_service = RichTextField(max_length=30000, verbose_name='Terms of service',
                                     default="Write Rules of your company in SiteManegmante", null=True, blank=True)
    tag = TaggableManager(verbose_name='Blog Tags')

    class Meta:
        verbose_name = 'Site setting'
        verbose_name_plural = 'Site Management'

    def __str__(self):
        return self.title


class BankAccount(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title ', default="Your Bank Account")
    public_key = models.CharField(max_length=1000, verbose_name='PUBLIC KEY', default="pk_test_TYooMQauvdEDq54NiTphI7jx")
    secret_key = models.CharField(max_length=1000, verbose_name='SECRET KEY', default="sk_test_4eC39HqLyjWDarjtT1zdp7dc")
    description = models.CharField(max_length=1000, verbose_name='Description', default="E-Commerce")
    currency = models.CharField(max_length=1000, verbose_name='Currency', default="usd")

    class Meta:
        verbose_name = 'Bank Account'
        verbose_name_plural = 'Bank Account'

    def __str__(self):
        return self.title

