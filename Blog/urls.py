from django.urls import path
from Blog.views import post_list, post_detail, post_share, post_emailing,\
    posts_list_by_tag, posts_list_by_category

# app_name = 'blog'
urlpatterns = [
    # Fetching all posts and passing to post_list templates.
    path('', post_list, name='post_list'),
    # Fetching single posts and passing to single_post templates.
    path('post/<str:slug>/<int:post_id>/', post_detail, name='post_detail'),
    # Fetching posts based on their tag and passing to post_list templates.
    path('tag/<slug:tag_slug>/', posts_list_by_tag, name='post_list_by_tag'),
    # Fetching posts based on their category and passing to post_list templates.
    path('category/<str:category_slug>/', posts_list_by_category, name='posts_list_by_category'),
    # searching url
    path('search/', post_list, name='search'),
    # Shearing post with your friends
    path('post_share/<int:post_id>/', post_share, name='post_share'),
    # back to the post that user shared it to their friend
    # todo: change format of url like post_share
    path('post_share/<int:post_id>/<title>/', post_emailing, name='post_share'),

]

