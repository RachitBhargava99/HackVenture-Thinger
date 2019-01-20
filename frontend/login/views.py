from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
import requests

from .forms import *

#a generalized helper function that consumes the forms for both login() and register()
def helper_function(request, isLogin):
	if request.method=="POST":
		form = LoginForm(request.POST) if isLogin else RegisterForm(request.POST)
		if form.is_valid():
			req = requests.post('https://thinger.appspot.com/login',json={'email':form.cleaned_data['email'],'password':form.cleaned_data['password']}).json() if isLogin else requests.post('https://thinger.appspot.com/register',json={'name':form.cleaned_data['name'],'email':form.cleaned_data['email'],'password':form.cleaned_data['password']}).json()
			print(req)
			if req['status'] == 0:
				messages.error(request,req['error'])
			else:
				if isLogin==True:
					request.session['auth_token'] =  req['auth_token']
					return redirect('index')
				else:
					return redirect('login:login')
	else:
		form=LoginForm() if isLogin else RegisterForm()
	return render(request,'login/login.html',{'form':form,'isLogin':isLogin})

def index(request):
	return redirect('login:login')

def login(request):
	return helper_function(request,True)
def register(request):
	return helper_function(request,False)
