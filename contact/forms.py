# -*- coding: utf-8 -*-
# @Author: Jonathan fu
# @Date:   2018-08-14 13:32:51
# @Last Modified by:   jonathan fu
# @Last Modified time: 2018-08-14 13:37:08
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name','last_name', 'email', 'text']   #需要显示的字段，实际上我都不用显示