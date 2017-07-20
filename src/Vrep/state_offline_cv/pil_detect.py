# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 20:46:55 2017

@author: Ming
"""

from PIL import Image
import pytesseract



image=Image.open("jiasim.png")
#im =image.convert("RGB") 
im =image.convert("L") 

threshold = 30

table = []
for i in range(256):
    if i < threshold:
        table.append(1)
    else:
        table.append(0)
out = im.point(table, '1')
#out.show()  
vcode=pytesseract.image_to_string(out,lang="chi_sim",config="-psm 8")      

print vcode  
