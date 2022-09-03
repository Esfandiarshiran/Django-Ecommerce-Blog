import requests
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from taggit.models import Tag
from Ecommerce_setting.models import SiteSetting


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'


def pagination(request, object_list, number_of_post=6):
    # Start pagination in function based view (FBV).
    paginator = Paginator(object_list, number_of_post)
    page_number = request.GET.get('page')
    try:
        posts_object = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page.
        page_number = 1
    except EmptyPage:
        # If page is out of range deliver last page of results.
        page_number = paginator.num_pages
    posts_object = paginator.page(page_number)
    # Passing all objects to templates for using them.
    return {'object_items': posts_object, 'pages': int(page_number)}


def post_list(request):
    # All Post in DB
    posts_list = Post.published.all()
    # searching
    search_form = SearchForm(request.POST or None)
    if search_form.is_valid():
        words = search_form.cleaned_data['words']
        posts_list = Post.searched.search(words)
    # Pagination
    temp_pagination = pagination(request=request, object_list=posts_list)

    contex = {
        'posts': temp_pagination['object_items'],
        'pages': temp_pagination['pages'],
        'search_form': search_form,
    }

    return render(request, 'blog/posts_list.html', contex)


def post_detail(request, post_id, slug):
    # Getting post with post id that given by urls (ex: /blog/post_id/post_title).
    post = get_object_or_404(Post, id=post_id)
    # increasing and saving visit count field for every visit to find the most visited or popular posts.
    post.visit_count += 1
    post.save(update_fields=['visit_count'])
    # fetch All comments for every single post.
    comments = post.comments.filter(active=True)
    new_comment = None
    # Making comment form and also saving in DB.
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # First we save in memory.
            new_comment = comment_form.save(commit=False)
            # Updating post field in comment table, connected with foreign key.
            new_comment.post = post
            # if user does not log in, will not be allowed to leave comment.
            if request.user.is_authenticated:
                new_comment.user = User.objects.get(id= request.user.id)
            else:
                return redirect('/account/login')
            new_comment.save()
    else:
        # As a GET method (ex: loading page) just we need empty Form.
        comment_form = CommentForm()
    # Number of comment for every single post.
    comments_count = comments.count()
    # All tags for every single post
    post_tags = post.tags.all()
    # Fetching related post based on its tags.
    # step 1: Finding ids of all tags for every single post.
    post_tag_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tag_ids).distinct().exclude(id=post.id)[:4]
    # Now it's time to sorting similar_post , finding the most similarity.
    # Don't forget to import 'Count'  ==> from django.db.models import Count.
    # what is annotate method? we can define variable during sending query set,to be exact/
    # adding a feature in every single field temporary.
    # In this line, similar_posts.annotate(same_tags=Count('tags') ==> we put number of tags in same_tags
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))[:4]
    # similar_posts= similar_posts.order_by('-same_tags', '-publish')
    # Passing all objects to templates for using them.
    # searching
    search_form = SearchForm(request.POST or None)
    if search_form.is_valid():
        words = search_form.cleaned_data['words']
        posts_list = Post.searched.search(words)
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comments_count': comments_count,
        'post_tags': post_tags,
        'similar_posts': similar_posts,
        'search_form': search_form,

    }
    return render(request, 'blog/single_post.html', context)


def posts_list_by_tag(request, tag_slug):
    tag = None
    # All published posts.
    posts_list = Post.published.all()
    # If we have tag_slug, (ex: /blog/tag/tag_slug), we find all post with the given tag_slug.
    if tag_slug:
        tag = Tag.objects.get(slug__iexact=tag_slug)
        if not tag:
            object_list = None
        else:
            object_list = posts_list.all().filter(tags__in=[tag])

    temp_pagination= pagination(request=request, object_list=object_list)
    contex = {
        'posts': temp_pagination['object_items'],
        'pages': temp_pagination['pages'],
    }
    return render(request, 'blog/posts_list.html', contex)


def posts_list_by_category(request, category_slug):
    # All published posts.
    posts_list = Post.published.all()
    # If we have category_slug, (ex: /blog/category/category_slug), we find all post with the given category_slug.
    if category_slug:
        posts_cat = Post.objects.filter(category__slug=category_slug)
        if not posts_cat:
            object_list = None
        else:
            object_list = posts_cat

    temp_pagination = pagination(request=request, object_list=object_list)
    contex = {
        'posts': temp_pagination['object_items'],
        'pages': temp_pagination['pages'],
    }
    return render(request, 'blog/posts_list.html', contex)


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # ... Send email
            # ......................................................................................................
            # First we call request.build_absolute_uri() to make domain name, and then we pass the post url
            post_url = request.build_absolute_uri(post.get_absolute_url())
            # Now user has the link of our post. it's time to ready subject. (ex: Sara recommend
            # you to read (post title))
            subject = f"{cd['name']} recommends you to read " \
                      f"{post.title}"
            # Now it's turn to ready message
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            # Eventually sending the Email by a built-in django method(send_mail)
            # sender = 'info@mySite.com'
            # receiver = to (every one who has been already filled out by user in the form (to) )
            send_mail(subject, message, 'info@mySite.com',
                      [cd['to']])
            # set send variable ti 'True when user sent the email'==> we need it to handel
            # situation in the post_share templates
            sent = True
            # just not that when project is under development, we can get it in terminal for testing
            ######## but as a final production you have to pass it to  your server SMPT or using your real gmail SMPT server ###########

    else:
        form = EmailPostForm()
    return render(request, 'blog/post_share.html', {'post': post, 'form': form, 'sent': sent})


def post_emailing(request, post_id, title):
    post = get_object_or_404(Post, id=post_id)

    context = {
        'post': post,
    }
    return render(request, 'blog/single_post.html', context)


