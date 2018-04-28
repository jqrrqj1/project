#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:Beck Lee time:2018/4/5

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

app_name ='[photoManage]'#添加命名空间语句

urlpatterns = [

    url(r'^showlist/$', views.showlist),
    url(r'^showlistDetail/$',csrf_exempt(views.showlistDetail)),
    url(r'^jstreeDetail/$', csrf_exempt(views.jstreeDetail)),#单页测试树

    url(r'^initSave/$',views.initSave),
    url(r'^savePhotoInfo/$',views.savePhotoInfo),
    url(r'^initModify/$',views.initModify),
    url(r'^modifyPhotoinfo/$',views.modifyPhotoinfo),
    url(r'^delPhotoinfo/$',views.delPhotoinfo),
]