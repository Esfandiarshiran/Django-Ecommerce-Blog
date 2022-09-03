from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from Blog.models import Post
from Ecommerce_products.models import Product


class LatestPostsFeed(Feed):
    title = 'My Blog'
    link = '/blog'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)


class LatestProductsFeed(Feed):
    title = 'My Products'
    link = '/products'
    description = 'New products of my website.'

    def items(self):
        return Product.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.features, 100)
