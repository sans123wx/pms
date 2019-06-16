from django import forms
from django.contrib.auth.hashers import check_password
from .models import *
from django.conf import settings
from .fnc import encrypt

class RecordForm(forms.Form):
    key = forms.CharField(label = '密匙' , widget = forms.PasswordInput(attrs = {'class':'form-control'}))
    title = forms.CharField(label = '名称', widget = forms.TextInput(attrs = {'class':'form-control'}))
    ip = forms.CharField(label = 'IP地址' , widget = forms.TextInput(attrs = {'class':'form-control'}))
    username = forms.CharField(label = '用户名' , widget = forms.TextInput(attrs = {'class':'form-control'}))
    pw = forms.CharField(label = '密码' , widget = forms.PasswordInput(attrs = {'class':'form-control'}))
    app_username = forms.CharField(label = '应用登录名' , widget = forms.TextInput(attrs = {'class':'form-control'}))
    app_pw = forms.CharField(label = '应用登录密码' , widget = forms.PasswordInput(attrs = {'class':'form-control'}))
    note = forms.CharField(label = '备注' , widget = forms.TextInput(attrs = {'class':'form-control'}))

    def clean_key(self):
        key = self.cleaned_data['key']
        if check_password(key , settings.ENCRYPTED_KEY):
            return key
        else:
            raise forms.ValidationError('密匙错误')
    
    def clean_username(self):
        key = self.cleaned_data.get('key')
        if key:
            username = self.cleaned_data.get('username')
            if username:
                username = username.strip()      
            else:
                username = 'unknown'
            encrypted_username = encrypt(username , key)
            return encrypted_username

    def clean_pw(self):
        key = self.cleaned_data.get('key')
        if key:
            pw = self.cleaned_data.get('pw')
            if pw:
                pw = pw.strip()      
            else:
                pw = 'unknown'
            encrypted_pw = encrypt(pw , key)
            return encrypted_pw
    
    def clean_app_username(self):
        key = self.cleaned_data.get('key')
        if key:
            app_username = self.cleaned_data.get('app_username')
            if app_username:
                app_username = app_username.strip()      
            else:
                app_username = 'unknown'
            encrypted_app_username = encrypt(app_username , key)
            return encrypted_app_username

    def clean_app_pw(self):
        key = self.cleaned_data.get('key')
        if key:
            app_pw = self.cleaned_data.get('app_pw')
            if app_pw:
                app_pw = app_pw.strip()      
            else:
                app_pw = 'unknown'
            encrypted_app_pw = encrypt(app_pw , key)
            return encrypted_app_pw

