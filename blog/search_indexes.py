# -*- coding: utf-8 -*-
# @Author: Jonathan fu
# @Date:   2018-07-29 12:53:01
# @Last Modified by:   jonathan fu
# @Last Modified time: 2018-07-29 13:56:33
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()