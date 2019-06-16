from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.views.decorators.http import require_POST
from django.http import HttpResponse , Http404

# Create your views here.

@login_required
def view(request):
    records = get_list_or_404(Record)
    context = {}
    context['records'] = records
    return render(request , 'record/view.html' , context)

@login_required
# @require_POST
def view_detail(request):
    records = get_list_or_404(Record)
    context = {}
    context['records'] = records
    context['key'] = 'nffy123'
    return render(request , 'record/view_detail.html' , context)
    # key = request.POST.get('key')
    # if check_password(key , settings.ENCRYPTED_KEY):
    #     records = get_list_or_404(Record)
    #     context = {}
    #     context['records'] = records
    #     context['key'] = key
    #     return render(request , 'record/view_detail.html' , context)
    # else:
    #     raise Http404('密匙错误')

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
            return render(request , 'record/success.html')
    else:
        form = RecordForm()
    context = {}
    context['form'] = form
    return render(request , 'record/create_record.html' , context)

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

@login_required
def edit_record(request):
    if request.method == 'POST':
        pass
    else:
        key = request.GET.get('key')
        context = {}
        if check_password(key , settings.ENCRYPTED_KEY):
            item_id = request.GET.get('item_id')
            record = get_object_or_404(Record , id = item_id)
            data = {
                'key':key,
                'title':record.title,
                'ip':record.ip,
                'username':record.username,
                'pw':record.pw,
                'app_username':record.app_username,
                'app_pw':record.app_pw,
                'note':record.note,
            }
            form = RecordForm(initial=data)
            context['form'] = form
            return render(request , 'record/create_record.html' , context)

        else:
            context['info'] = '密匙错误'
            return render(request , 'record/success.html' , context)
