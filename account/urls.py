from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('login' , login , name = 'login'),
    path('passwordchange' , PasswordChangeView.as_view(template_name = 'account/passwordchange.html') , name = 'passwordchange'),
    path('passwordchangedone' , PasswordChangeDoneView.as_view(template_name = 'account/passwordchangedone.html') , name = 'password_change_done'),
    path('logout' , logout , name = 'logout'),
    path('ajax_post_captcha' , ajax_post_captcha , name = 'ajax_post_captcha'),

]