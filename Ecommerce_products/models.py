from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import Q
from Ecommerce_Product_Category.models import ProductsCategory
from django.contrib.auth.models import User
from django.utils.text import slugify


# Hot Item

###### Picturrs size on home page ###########
# 1900 * 700 ======> Frist and bigest Banner
# 550 * 750 ========> Trending Item
# 550 * 750 ========> Hot Item
# 370 * 300 =========? Blog items in home page
###### Picturrs size on products  page ###########
# 550 * 750 ========> size pf products' pics on the products page
# 75 * 75 ===========> in the righr slide bar on products page
###################################################################


# Create your models here.

# Create Upload and Download file and pics
import os


# =====Start Process to get the picture sent by user, and changing the name======
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_Gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries{final_name}"


# =====End process  to get the picture sent by user, and changing the name======


# ================== Define Product Model (Table) ========================

class ProductManager(models.Manager):
    # After Product.object. in the view we have access to this function
    # for Example instead of Product.object.all() we can write Product.object.get_active_products()
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_active_products_slider(self):
        return self.get_queryset().filter(slider=True)

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(category__name__icontains=category_name, active=True)

    def get_by_Id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


# 1900 * 700
class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    features = RichTextField(max_length=5000, verbose_name="features", default="")
    description = RichTextField(max_length=30000)
    slug = models.SlugField(max_length=400, blank=True)
    price = models.FloatField()
    discount = models.IntegerField(null=True)
    picture = models.ImageField(upload_to=upload_image_path, null=False, blank=False, verbose_name='Picture')
    active = models.BooleanField(default=True, verbose_name="Availability")
    is_free = models.BooleanField(default=False, verbose_name="is free?")
    zip_file = models.FileField(upload_to='products_file' ,verbose_name='Upload Product(Zip File)', default="")
    hotitem = models.BooleanField(default=True, verbose_name='Hot-items')
    category = models.ManyToManyField(ProductsCategory, blank=False)
    recommend = models.BooleanField(default=True, verbose_name="Show in recommendation products")
    visit_count = models.IntegerField(default=0, verbose_name='Visiting Number')
    objects = ProductManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"
        # Sample:  products/2/Insta-bot


############# define slider model(Tabale) for changing sliderbar in admin panel #######


class SliderPicture(models.Model):
    # The size of pic must be exactly 1900 * 700
    title = models.CharField(max_length=150, verbose_name="Name")
    link = models.URLField(max_length=200, verbose_name="Link")
    description = models.TextField(verbose_name="Description", default="")
    picture = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                                verbose_name='Slider-Picture')


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name="Name")
    picture = models.ImageField(upload_to=upload_Gallery_image_path, null=True, blank=True,
                                verbose_name='Slider-Picture')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")


