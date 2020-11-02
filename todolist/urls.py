# -*- coding: utf-8 -*-
# @Author: Jonathan fu
# @Date:   2018-08-02 09:32:12
# @Last Modified by:   jonathan fu
# @Last Modified time: 2018-08-02 09:33:41
from django.conf.urls import url

from . import views

app_name = 'todolist'
urlpatterns = [
    url(r'^todolist/$', views.todolist, name='todolist'),
]