#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:blackfeather

import django
import os,sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TargetRangeWeb.settings")
django.setup() #os.environ['DJANGO_SETTINGS_MODULE']