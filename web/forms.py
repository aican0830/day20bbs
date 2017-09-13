#!/usr/bin/env python
# -*- coding:utf-8  -*-

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=5)
    summary = forms.CharField(max_length=255,min_length=5)
    head_img = forms.ImageField()
    category_id = forms.IntegerField()
    content = forms.CharField(min_length=10)
