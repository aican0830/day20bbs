# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
import models
from web.forms import ArticleForm
import os
# Create your views here.

def index(request):

    articles = models.Article.objects.all()
    return render(request,'index.html',{'articles':articles})


def category(request,category_id):
    print ("-->",category_id)
    articles = models.Article.objects.filter(category_id=category_id)
    return render(request, 'index.html', {'articles': articles})


def article_detail(request,article_id):
    try:
        article_obj = models.Article.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
        return render(request,'404.html',{'err_msg':u'文章不存在！'})
    return render(request,'article.html',{'article_obj':article_obj})


def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def acc_login(request):
    err_msg = ''

    print request.POST
    if request.method =='POST':
        print "user authention..."
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            err_msg = "Wrong username or password!"
    return render(request,'login.html',{'err_msg':err_msg})



def new_article(request):
    if request.method =='POST':
        print request.POST
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            print ("--form.data:",form.data)
            form_data = form.cleaned_data
            form_data['author_id'] = request.user.userprofile.id

            new_img_path = handle_uploaded_file(request,request.FILES['head_img'])
            form_data['head_img'] = new_img_path
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(request,'new_article.html',{'new_article_obj':new_article_obj})
        else:
            print ('err_msg',form.errors)
    category_list = models.Category.objects.all()
    return render(request,'new_article.html',{'category_list':category_list})




def handle_uploaded_file(request,f):
    print ("--->",f.name)
    base_img_upload_path = 'statics/imgs'
    user_path = "%s/%s" %(base_img_upload_path,request.user.userprofile.id)
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    with open('%s/%s' %(user_path,f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    alias_path = "/static/imgs"
    return '/static/imgs/%s/%s' %(request.user.userprofile.id,f.name)