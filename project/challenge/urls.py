#coding=utf-8
from django.conf.urls import patterns, include, url
from challenge import views

urlpatterns = patterns('',
					(r'^$', views.base),
                    (r'makequestion/$',views.makequestion),
					(r'makequestion/success_question/$',views.success_question),
                    (r'web/$',views.challenge_web),
                    (r'web_start/$',views.web_start),
                    (r'web_restart/$',views.web_restart),
)           
