from django.shortcuts import render_to_response
from form import RegiserForm,LoginForm

# Create your views here.
def welcome(request):
	return render_to_response('welcome.html')