#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:blackfeather


import django
import os,sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TargetRangeWeb.settings")
django.setup() #os.environ['DJANGO_SETTINGS_MODULE']

from web import models
#往数据库添加数据：链接数据库，操作，关闭数据库
models.UserInfo.objects.create(username='fucker',email='fucker@live.com',mobile_phone='13888888888',password='12345678')

