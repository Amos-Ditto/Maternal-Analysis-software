from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def index(request):
	context = {}
	return render(request, 'dapapp/index.html', context)

def signin(request):
	form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	context = {'form': form}
	return render(request, 'dapapp/signin.html', context)


def homepage(request):
	context = {}
	return render(request, 'dapapp/home.html', context)

def forms(request):
	context = {}
	return render(request, 'dapapp/reports.html', context)