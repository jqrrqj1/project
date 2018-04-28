#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:Beck Lee time:2018/4/6
from django.conf.urls import url
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views
app_name ='[account]'#添加命名空间语句
urlpatterns = [
    # url(r'^login/$',views.user_login,name="user_login"),#自定义的登陆
    # url(r'^login/$',auth_views.login,name='user_login'),#django内置登陆
    url(r"^login/$",auth_views.login,{"template_name":"registration/login.html"},name='user_login'),
    # url(r'^logout/$',auth_views.logout,name='user_logout'),
    url(r"^logout/$",auth_views.logout,{"template_name":"account/logout.html"},name='user_logout'),
]