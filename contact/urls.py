# -*- coding: utf-8 -*-
# @Author: Jonathan fu
# @Date:   2018-08-14 13:53:34
# @Last Modified by:   jonathan fu
# @Last Modified time: 2018-08-14 14:55:42
from django.conf.urls import url

from . import views

app_name = 'contact'
urlpatterns = [
    url(r'^contact/ok/$', views.contact, name='contact'),
]