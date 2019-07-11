#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:56:38 2019

@author: brady
"""

from PIL import Image
import numpy as np

def get_data(im, x_range, x_offset, y_range, y_offset):
    x_data = np.array([])
    y_data = np.array([])
    width, height = im.size
    im = im.convert('1')
    for x in range(width):
        for y in range(height):
            if im.getpixel((x, y)) == 0:
                x_data = np.append(x_data, x)
                y_data = np.append(y_data, height - y)
                break
    x_data = (x_data / width) * x_range + x_offset
    y_data = (y_data / height) * y_range + y_offset
    return x_data, y_data

im = Image.open('movies/600w/chromatogramAsset 1.png')
x_data, y_data = get_data(im,600/1,1,200-0,0)

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n*multiplier)/multiplier

for i in range(len(x_data)):
    print(truncate(x_data[i]))

