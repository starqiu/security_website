#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django_bt.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from django.core.exceptions import ObjectDoesNotExist
   
class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"帐号",
        max_length=20,
        error_messages={'required': '请输入帐号'},
        widget=forms.TextInput(
            attrs={
                'class':u"form-control",
            }
        ),
    )    
    password = forms.CharField(
        required=True,
        label=u"密码",
        max_length=20,
        error_messages={'required': u'密码不能为空'},
        widget=forms.PasswordInput(
            attrs={
                'class':u"form-control" ,
            }
        ),
    )   
    passwordag = forms.CharField(
        required=True,
        label=u"再次输入密码",
        max_length=20,
        error_messages={'required': u'密码不能为空'},
        widget=forms.PasswordInput(
            attrs={
                'class':u"form-control",
            }
        ),

    )
    emaildata = forms.EmailField(
        required = False,
        label = u"邮箱",
        max_length=30,
        error_messages={'valid':u'请按格式输入'},
        widget = forms.TextInput(
            attrs={
                'placeholder':u"请输入电子邮箱（可选）",
                'class':u"form-control",            
                }

        ),

    )


    def clean_data(self):#放在第一个执行
        if not self.is_valid():
            raise forms.ValidationError(u"error")
        else:
            cleaned_data = super(RegisterForm, self).clean() 
        return cleaned_data

    def clean_passwordag(self):
        if 'passwordag' in self.cleaned_data:
            password=self.cleaned_data['password']
            passwordag=self.cleaned_data['passwordag']
            if password!=passwordag:
                raise forms.ValidationError('两次输入密码不一致！')
            return passwordag
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('用户名已经存在！')



