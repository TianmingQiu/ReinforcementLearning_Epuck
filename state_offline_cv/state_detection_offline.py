# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 21:39:00 2017

@author: Ming
"""

from PIL import Image
import pytesseract
import cv2
import numpy as np  


cv2_img = cv2.imread('jiasim.png') 

redLower = np.array([0, 100, 100])  
redUpper = np.array([20, 255, 255])  

hsv = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2HSV)  
mask = cv2.inRange(hsv, redLower,redUpper) 
mask = cv2.dilate(mask, None, iterations=2)  
#mask = cv2.erode(mask, None, iterations=2) 
pil_img = Image.fromarray(mask)
#pil_img.show()
im =pil_img.convert("L") 
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(1)
    else:
        table.append(0)
out = im.point(table, '1')
out.show()

vcode=pytesseract.image_to_string(out,lang="chi_sim",config="-psm 8")      

print vcode  