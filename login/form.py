#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

class RegiserForm(forms.Form):
	family_name = forms.CharField()
	given_name = forms.CharField()
	net_name = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField()
	password2 = forms.CharField()
	introducer = forms.CharField(required=False)

class LoginForm(forms.Form):  
    email = forms.EmailField()  
    password = forms.CharField(widget=forms.PasswordInput)  