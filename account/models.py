from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInformation(models.Model):
    user = models.OneToOneField(User , on_delete = models.DO_NOTHING , verbose_name = '对应账号')
    nick_name = models.CharField(max_length = 50 , verbose_name = '用户名')