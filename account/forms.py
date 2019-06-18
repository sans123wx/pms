from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(label = '用户名' , widget = forms.TextInput(attrs = {'class':'form-control'}))
    password = forms.CharField(label = '密码' , widget = forms.PasswordInput(attrs = {'class':'form-control'}))
    captcha = CaptchaField()

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username = username , password = password)
        if user:
            self.cleaned_data['user'] = user
            return self.cleaned_data
        else:
            raise forms.ValidationError('用户名或密码不正确')

class CaptchaForm(forms.Form):
    captcha = CaptchaField()


