# -*- coding: utf-8 -*-
# @Author: Jonathan fu
# @Date:   2018-08-04 18:39:19
# @Last Modified by:   jonathan fu
# @Last Modified time: 2018-08-04 20:49:43
from django.conf.urls import url

from . import views

app_name = 'hydrogen'
urlpatterns = [
    url(r'^$', views.hydrogen, name='hydrogen'),
]