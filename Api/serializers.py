from rest_framework import serializers
from Blog.models import Post
from Ecommerce_products.models import Product


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'create_date', 'publish_date', 'visit_count', 'status', 'picture', 'body')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'features', 'price', 'discount', 'is_free', 'zip_file', 'description')
