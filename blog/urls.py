from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^contact/', 'blog.views.ContactView', name = 'contact'),
    #url(r'^contact/', FormView.as_view(form_class=Contact, success_url='/thanks/'),
    url(r'^category/$', 'blog.views.getCategory', name = 'category'),
    url(r'^category/(?P<categorySlug>\S+)/$', 'blog.views.getCategorySearch', name = 'category_search'),
    url(r'^tag/(?P<tagSlug>\S+)/$', 'blog.views.getTagSearch', name = 'tag_search'),
    url(r'^about/$', 'blog.views.about', name = 'about'),
    url(r'^page/(\d+)/$', 'blog.views.articles', name="home"),
    url(r'^$', 'blog.views.articles', name="home"),
    url(r'^(?P<slug>\S+)/$', 'blog.views.article', name="article"),
]