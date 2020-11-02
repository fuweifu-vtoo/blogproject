# -*- coding: utf-8 -*-
# @Author: Jonathan fu
# @Date:   2018-07-26 20:29:42
# @Last Modified by:   jonathan fu
# @Last Modified time: 2018-07-26 20:43:53
from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]