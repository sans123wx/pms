from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):
    title = models.CharField(max_length = 50 , verbose_name = '名称')
    ip = models.CharField(max_length = 100 , verbose_name = 'IP地址')
    username = models.CharField(max_length = 100 , verbose_name = '用户名' , default = '-')
    pw = models.CharField(max_length = 100 , verbose_name = '密码' , default = '-')
    app_username = models.CharField(max_length = 100 , verbose_name = '应用登录名' , default = '-')
    app_pw = models.CharField(max_length = 100 , verbose_name = '应用登录密码' , default = '-')
    note = models.CharField(max_length = 500 , verbose_name = '备注' , default = '-')
    created_time = models.DateTimeField(auto_now_add = True , verbose_name = '创建时间')
    created_user = models.ForeignKey(User , verbose_name = '创建人' , on_delete = models.DO_NOTHING , related_name = 'created_user')
    update_time = models.DateTimeField(auto_now = True ,verbose_name = '修改时间')
    update_user = models.ForeignKey(User , verbose_name = '修改人' , on_delete = models.DO_NOTHING , related_name = 'update_user')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '密码管理'