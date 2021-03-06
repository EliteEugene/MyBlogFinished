"""MyBlog URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from filebrowser.sites import site

# Enable the admin
admin.autodiscover()

urlpatterns = [
    #url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/comments/', include('django_comments.urls')),
    url(r'^search/', include('haystack.urls', namespace="search")),
    url(r'^auth/', include('loginsys.urls')),
    #url(r'^tinymce/', include('tinymce.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^contact/', include('contact.urls', namespace="contact")),
    url(r'^', include('blog.urls', namespace="blog")),

] 

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))