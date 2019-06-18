from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.views.decorators.http import require_POST
from django.http import HttpResponse , Http404
from account.forms import CaptchaForm
from ratelimit.decorators import ratelimit
# Create your views here.

@login_required
def view(request):
    records = get_list_or_404(Record)
    context = {}
    context['records'] = records
    return render(request , 'record/view.html' , context)

@ratelimit(key = 'ip' , rate = '6/h' , block = True)
@ratelimit(key = 'post:key' , rate = '6/h' , block = True)
@login_required
@require_POST
def view_detail(request):
    context = {}
    form = CaptchaForm(request.POST)
    if form.is_valid():
        key = request.POST.get('key')
        if check_password(key , settings.ENCRYPTED_KEY):
            records = get_list_or_404(Record)
            context['records'] = records
            context['key'] = key
            return render(request , 'record/view_detail.html' , context)
        else:
            context['info'] = '密匙错误'
    else:
        context['info'] = '验证码错误'
    return render(request , 'record/success.html' , context)

@ratelimit(key = 'ip' , rate = '6/h' , block = True)
@ratelimit(key = 'post:key' , rate = '6/h' , block = True)
@login_required
def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            Record.objects.create(title = form.cleaned_data['title'],
                                  ip = form.cleaned_data['ip'],
                                  username = form.cleaned_data['username'],
                                  pw = form.cleaned_data['pw'],
                                  app_username = form.cleaned_data['app_username'],
                                  app_pw = form.cleaned_data['app_pw'],
                                  note = form.cleaned_data['note'],
                                  created_user = request.user,
                                  update_user = request.user
                                  )
            return render(request , 'record/success.html' , {'info':'创建成功'})
    else:
        form = RecordForm()
    context = {}
    context['form'] = form
    return render(request , 'record/create_record.html' , context)

@ratelimit(key = 'ip' , rate = '6/h' , block = True)
@ratelimit(key = 'post:key' , rate = '6/h' , block = True)
@login_required
@require_POST
def delete_record(request):
    key = request.POST.get('key')
    context = {}
    if check_password(key , settings.ENCRYPTED_KEY):
        item_id = request.POST.get('item_id')
        reocrd = get_object_or_404(Record , id = item_id)
        reocrd.delete()
        context['info'] = '操作成功'
    else:
        context['info'] = '密匙错误'
    return render(request , 'record/success.html' , context)

@ratelimit(key = 'ip' , rate = '6/h' , block = True)
@ratelimit(key = 'post:key' , rate = '6/h' , block = True)
@login_required
@require_POST
def edit_record(request):
    context = {}
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():   
            item_id = request.POST.get('item_id')
            record = get_object_or_404(Record , id = item_id)
            record.title = form.cleaned_data['title']
            record.ip = form.cleaned_data['ip']
            record.username = form.cleaned_data['username']
            record.pw = form.cleaned_data['pw']
            record.app_username = form.cleaned_data['app_username']
            record.app_pw = form.cleaned_data['app_pw']
            record.note = form.cleaned_data['note']
            record.save()
            context['info'] = '修改成功'
        else:
            context['info'] = '发生错误，请检查密匙是否正确'

    else:
        context['info'] = '非法访问'
    return render(request , 'record/success.html' , context)

