from Blog.models import Post
from .serializers import PostSerializer, ProductSerializer
from rest_framework import generics, permissions
from .permissions import IsadminOrReadOnly
from Ecommerce_products.models import Product


class PostsList(generics.ListCreateAPIView):
    permission_classes = (IsadminOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsadminOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProductsList(generics.ListCreateAPIView):
    permission_classes = (IsadminOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsadminOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# .../dj-rest-auth/login
# .../dj-rest-auth/logout
# .../dj-rest-auth/password/reset
# .../dj-rest-auth/password/reset/confirm
#.../api/v1/rest-auth/registration
