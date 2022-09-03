from Blog.models import PostsCategory, Post
from Ecommerce_setting.models import SiteSetting

posts = Post.published.all()


# All Blog category
def all_posts_category_context(request):
    blog_categories = PostsCategory.objects.all()
    return dict(blog_categories_context=blog_categories)


# Last 3 recently posted
def recent_posts_context(request):
    recent_posts = posts.order_by('-create_date')[:3]
    return dict(recent_posts_context=recent_posts)


# All Blog tags that was defined in the Site Management by admin.
def blog_tags_context(request):
    blog_tags = SiteSetting.objects.first()
    blog_tags = blog_tags.tag.all()
    return dict(blog_tags_context=blog_tags)


# Most 3 popular posts based on visiting count, increasing in every visit in post_detail.
def popular_posts_context(request):
    popular_posts = posts.order_by('-visit_count')[:3]
    return dict(popular_posts_context=popular_posts)
