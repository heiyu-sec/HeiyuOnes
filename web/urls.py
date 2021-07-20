#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:blackfeather
from django.conf.urls import url,include
from web.views import account
from web.views  import home
from web.views  import project

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
    url(r'^login/sms/$', account.login_sms, name='login_sms'),
    url(r'^send/sms/$', account.send_sms, name='send_sms'),
    url(r'^login/$', account.login, name='login'),
    url(r'^image/code/$', account.image_code, name='image_code'),
    url(r'^index/$', home.index, name='index'),
    url(r'^logout/$', account.logout, name='logout'),

    #项目管理
    url(r'^project/list/$', project.project_list, name='project_list'),
    # /project/star/my/1
    # /project/star/join/1

]