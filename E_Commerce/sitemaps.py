from django.contrib.sitemaps import Sitemap
from Ecommerce_products.models import Product
from Blog.models import Post


class PostSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.update_date


class ProductSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.9

    def items(self):
        return Product.objects.all()

