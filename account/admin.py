from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(UserInformation)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('user' , 'nick_name')