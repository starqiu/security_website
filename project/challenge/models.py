#!/usr/bin/evn python
#coding=utf-8

from django.db import models

class User(models.Model):
    UAccount = models.CharField(max_length=20)#帐号名
    UEmail = models.EmailField(blank=True,max_length=30)#邮箱
    Uis_challenging = models.CharField(max_length=20)#是否有未完成的挑战			
    UPrivilege = models.CharField(max_length=20)#权限,1为学生，2为老师
    QSection = models.CharField(max_length=20)#记录答题部分
    QNumber = models.CharField(max_length=20)#记录答题编号
    WebScore = models.CharField(max_length=20)#记录web闯关答题分数
    class Meta:
        abstract = True     

	
class Question(models.Model):
    QTitle = models.CharField(max_length=100)#题目标题
    QSectionFir = models.CharField(max_length=20)#一级目录,1代表web安全，2代表信息安全 
    QSectionSec = models.CharField(max_length=20)#二级目录    
    QNumber = models.CharField(max_length=30)#题目编号，题目编号=一级目录x100000+二级目录x10000+id
    QScore = models.CharField(max_length=30)#题目分值
    QContent = models.TextField(max_length=10000)#题目内容
    QAnswerA = models.CharField(max_length=100)#答案A
    QAnswerB = models.TextField(max_length=100)#答案B
    QAnswerC = models.TextField(max_length=100)#答案C
    QAnswerD = models.TextField(max_length=100)#答案D
    QCorrect = models.TextField(max_length=10)#正确答案的编号
    QTeacher = models.CharField(max_length=20)#出题人
    QRate = models.CharField(max_length=20,blank=True)#正确率
    def __unicode__(self):
        return self.QTitle

class Teacher(User):
    #Qstatus = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.UAccount
    
class Student(User):

    def __unicode__(self):
        return self.UAccount
