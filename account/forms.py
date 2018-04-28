#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author:Beck Lee time:2018/4/6
from django import  forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)