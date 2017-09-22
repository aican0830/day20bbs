# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
#import models
from web import models

#admin界面只限制第一列，我们想让他显示id之类的列的时候，重新定义类
class CategroyAdmin(admin.ModelAdmin):
    list_display = ('id','name')
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','hidden','publish_date')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','parent_comment','comment','date')
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Category,CategroyAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.ThumbUp)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)