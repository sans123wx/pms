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
@require_POST
def view_detail(request):
    key = request.POST.get('key')
    if check_password(key , settings.ENCRYPTED_KEY):
        records = get_list_or_404(Record)
        context = {}
        context['records'] = records
        context['key'] = key
        return render(request , 'record/view_detail.html' , context)
    else:
        raise Http404('密匙错误')

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
                                  created_user = request.user,
                                  update_user = request.user
                                  )
            return HttpResponse('success')
    else:
        form = RecordForm()
    context = {}
    context['form'] = form
    return render(request , 'record/create_record.html' , context)