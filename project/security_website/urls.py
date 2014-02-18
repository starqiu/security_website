#coding=utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',	
    (r'^$', views.index),#主页
    (r'^register/',views.register_index),#注册
    (r'^admin/', include(admin.site.urls)),#admin
    (r'^login/',views.login),#登陆
    (r'^logout/',views.logout),#注销
    (r'^test/',views.test),#测试
    (r'^error/',views.error),#注册错误信息
    url(r'^clg/',include('challenge.urls')),#挑战
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),#配置静态文件




    # Examples:
    # url(r'^$', 'security_website.views.home', name='home'),
    # url(r'^security_website/', include('security_website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
