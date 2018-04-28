#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:Beck Lee time:2018/4/6
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

from .forms import LoginForm

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("登陆成功！")
            else:
                return HttpResponse("对不起，用户名或密码错误！")
        else:
            return HttpResponse("登陆不成功！")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})