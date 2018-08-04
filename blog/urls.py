from django.conf.urls import url
from django.conf.urls import include
from django.core.urlresolvers import reverse

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^blog/$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^full_width/$', views.full_width, name='full_width'),
    url(r'^about/$', views.about, name='about'),
    #url(r'^search/$', views.search, name='search'),
]
