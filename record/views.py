from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect
from .models import *
# from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.views.decorators.http import require_POST
from django.http import HttpResponse

# Create your views here.

@login_required
def view(request):
    records = get_list_or_404(Record)
    context = {}
    context['records'] = records
    return render(request , 'record/view.html' , context)