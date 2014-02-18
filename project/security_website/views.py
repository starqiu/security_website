#coding=utf-8
from django.shortcuts import render_to_response,render,get_object_or_404    
from django.http import HttpResponse, HttpResponseRedirect    
from django.contrib.auth.models import User    
from django.contrib import auth  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm
from django.template.context import RequestContext  
from django import forms
from challenge.models import Question,Teacher,Student
from forms import RegisterForm
from django.forms.formsets import formset_factory  
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  
from django.contrib.sessions.models import Session
from django_bt.widgets import BootstrapUneditableInput  
from django.contrib.auth.decorators import login_required#login装饰器


def index(request):
    request.session["is_teacher"]=False
    return render_to_response('index.html',context_instance=RequestContext(request))



def register_index(request):
    form = None
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data#转化为python可处理的格式
            username = data['username']
            user=User.objects.create(
                username = data['username'],
                password = data['password'],
                email =data['emaildata'],
                is_active =True,
            )            
            user.set_password(data['password'])#加上这句话后可以使密码hash加密后存储在数据库中
            user.save()
            user=auth.authenticate(username=data['username'],password=data['password'])
            auth.login(request,user)#注册完登陆
            request.session['Uname']=username#保存登陆者名字
            request.session['is_teacher']=False#不能直接注册为老师
            student = Student.objects.create(
                UAccount = data['username'],
                UEmail=data['emaildata'],
                Uis_challenging = 0,
                UPrivilege =1,#1为学生，2为老师
                QSection =0,
                QNumber = 0,
                WebScore = 0,#当有别的挑战加入时，在此处更新代码   
            )
            student.save()            
    
            return render_to_response('RegisterS.html',context_instance=RequestContext(request))
        else:
            return render_to_response('register.html',context_instance=RequestContext(request,{'form': form}))
    else:
        form = RegisterForm()
        return render_to_response('register.html',context_instance=RequestContext(request,{'form': form}))


def error(request):
    pass

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        request.session['Uname']=username#保存登陆者名字
        if Teacher.objects.filter(UAccount=username).exists():        
            request.session['is_teacher']=True
            
        else:
            request.session['is_teacher']=False
            
        return render_to_response('index.html',  context_instance=RequestContext(request))
    else:
        return render_to_response('index.html',  context_instance=RequestContext(request,{'password_is_wrong':True}))
        
def logout(request):
    auth.logout(request)
    request.session["is_teacher"]=False
    request.session['Uname']=False
    return render_to_response('index.html', context_instance = RequestContext(request))

def test(request):
    return render_to_response("clg.html" , context_instance=RequestContext(request))


