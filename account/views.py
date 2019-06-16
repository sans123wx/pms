from django.shortcuts import render , redirect
from .forms import *
from django.contrib import auth
from django.urls import reverse
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            auth.login(request , user)
            return redirect(reverse('view'))

    else:
        form = LoginForm()
    context = {}
    context['form'] = form
    return render(request , 'account/login.html' , context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))