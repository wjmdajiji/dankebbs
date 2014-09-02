#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

TOPIC_CHOICES = (
	('suggestion',u'新功能建议'),
	('bug',u'错误'),
	)

class ContactForm(forms.Form):
	sender = forms.EmailField(required=False)
	topic = forms.ChoiceField(choices = TOPIC_CHOICES)
	title = forms.CharField()
	content = forms.CharField(widget=forms.Textarea())