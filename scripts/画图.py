#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:blackfeather

from PIL import Image,ImageDraw

img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))

with open('code.png','wb') as f:
    img.save(f,format='png')