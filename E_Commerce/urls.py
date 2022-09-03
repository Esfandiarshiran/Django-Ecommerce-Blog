"""E_Commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from .views import home_page, header, footer
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, ProductSitemap
from .feeds import LatestPostsFeed,LatestProductsFeed
# from django.urls import re_path as url
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

sitemaps = {
    'products': ProductSitemap,
    'posts': PostSitemap,

}

urlpatterns = [
    # Main project's Paths
    path('', home_page),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
    # Api APP Paths
    path('api/v1/', include('Api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/schema/', get_schema_view(title="Ecommerce API")),
    path('api/core-docs/', include_docs_urls(title= 'Ecommerce API')),
    path('api/docs/', get_swagger_view(title='Ecommerce API')),
    # Captcha APP Paths
    path('captcha/', include('captcha.urls')),
    # Ecommerce_Account's APP Paths
    path('account/', include('Ecommerce_Account.urls')),
    # Blog
    path('blog/', include('Blog.urls')),
    # Ecommerce_User_Dashboard
    path('dashboard/', include('Ecommerce_User_Dashboard.urls')),
    # Ecommerce_products' App
    path('', include('Ecommerce_products.urls')),
    # Ecommerce_Contact' App
    path('', include('Ecommerce_Contact.urls')),
    # Ecommerce_order' App
    path('', include('Ecommerce_order.urls')),
    # Ecommerce_about_us App
    path('', include('Ecommerce_about_us.urls')),
    path('feed/', LatestProductsFeed(), name='feed'),
    path('blog/feed', LatestPostsFeed(), name='feed'),
    #  site maps for Products in Ecommerce as well as post in blog
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    # Django Admin Path
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add root media files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# -------It was made by Esfandiar shiran ---- esf.shiran@gmail.com
