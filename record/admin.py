from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('title' , 'ip' , 'username' , 'pw' , 'app_username' , 'app_pw' , 'note' , 'created_time' , 'created_user' ,
                    'update_time' , 'update_user')