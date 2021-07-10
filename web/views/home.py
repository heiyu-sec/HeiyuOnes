#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:blackfeather

from django.shortcuts import render


def index(request):

    return render(request,'index.html')