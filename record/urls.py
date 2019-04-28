from django.urls import path
from .views import *

urlpatterns = [
    path('' , view , name = 'view'),
    path('view_detail' , view_detail , name = 'view_detail'),
    path('create_record' , create_record , name = 'create_record'),
]