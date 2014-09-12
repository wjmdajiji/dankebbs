#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

# Create your views here.
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
	else:
		form = ContactForm()
	return render_to_response('contact.html', {'form' : form})
