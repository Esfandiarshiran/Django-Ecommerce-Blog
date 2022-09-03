from django.urls import path
from .views import PostsList, PostDetail, ProductsList, ProductDetail

urlpatterns = [

    path('posts-list/', PostsList.as_view()),
    path('post-detail/<int:pk>/', PostDetail.as_view()),
    path('products-list/', ProductsList.as_view()),
    path('product-detail/<int:pk>/', ProductDetail.as_view()),

]
