#coding=utf-8
from django.shortcuts import render_to_response,render,get_object_or_404    
from django.http import HttpResponse, HttpResponseRedirect    
from django.contrib.auth.models import User    
from django.contrib import auth  
from django.contrib import messages  
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template.context import RequestContext  
from challenge.models import Question,Teacher,Student 
from django.forms.formsets import formset_factory  
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  
from django.contrib.sessions.models import Session  
from django_bt.widgets import BootstrapUneditableInput  
#from django.contrib.auth.decorators import login_required


def base(request):
    tag = request.session['is_teacher']
    if tag==False:
        return render_to_response("challenge.html" , context_instance=RequestContext(request,{'is_teacher':False}))
    else:
        return render_to_response("challenge.html" , context_instance=RequestContext(request,{'is_teacher':True}))

def makequestion(request):
    return render_to_response("Cquestion.html",context_instance=RequestContext(request,{'is_teacher':True}))

def success_question(request):
    if request.method=='POST':    
        sort_primary = int(request.POST.get("classify",''))#题目类型编号
        sort_two = sort_primary%(10)
        sort_one = (sort_primary-sort_two)/10    
        Tname = request.session['Uname']    
        question = Question(
            QTitle = request.POST.get("title",''),                              
            QSectionFir=sort_one,
            QSectionSec=sort_two,
            QNumber=0,#先赋值为0，存入数据库后使用表id赋值
            QScore=request.POST.get("score",''),
            QContent=request.POST.get("content",''),
            QAnswerA=request.POST.get("ida",''),
            QAnswerB=request.POST.get("idb",''),
            QAnswerC=request.POST.get("idc",''),
            QAnswerD=request.POST.get("idd",''),
            QCorrect=request.POST.get("Correct",''),
            QTeacher=Tname,
            QRate=0,
            )    
        question.save()
        question.QNumber=sort_one*100000+sort_two*10000+question.id
        question.save()    
        
    
    return render_to_response("success_question.html",context_instance=RequestContext(request,{'is_teacher':True}))

def challenge_web(request):
    Tname = request.session['Uname']
    is_teacher=False#判断是否是老师
    if Teacher.objects.filter(UAccount=Tname).exists():
        teacher = Teacher.objects.filter(UAccount=Tname)[0]
        if teacher.Uis_challenging:#判断是否有未完成的挑战
            is_new=True
            return  render_to_response("challengingpre.html",context_instance=RequestContext(request,{'is_new':is_new}))
        else:
            is_new =False#没有未完成的挑战
            return  render_to_response("challengingpre.html",context_instance=RequestContext(request,{'is_new':is_new}))
    else:
        student = Student.objects.filter(UAccount=Tname)[0]     
        if student.Uis_challenging:
            is_new=True          
            return render_to_response("challengingpre.html",context_instance=RequestContext(request,{'is_new':is_new}))
        else:
            is_new=False##没有未完成的挑战
            return  render_to_response("challengingpre.html",context_instance=RequestContext(request,{'is_new':is_new}))


def web_start(request):
    pass

def web_restart(request):
    pass



    

