from django.shortcuts import render , redirect
from .forms import *
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ratelimit.decorators import ratelimit
# Create your views here.

@ratelimit(key = 'ip' , rate = '6/h' , block = True)
@ratelimit(key = 'post:username' , rate = '6/h' , block = True)
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

@login_required
def ajax_post_captcha(request):
    form = CaptchaForm()
    return render(request , 'account/captcha.html' , {'form':form})