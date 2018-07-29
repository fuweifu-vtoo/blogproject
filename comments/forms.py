# -*- coding: utf-8 -*-
# @Author: Jonathan fu
# @Date:   2018-07-26 20:27:55
# @Last Modified by:   jonathan fu
# @Last Modified time: 2018-07-26 20:28:30

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']