# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:28:54 2022

@author: Jun
"""

#Saca la cantidad de vocales que hay y cuantas hay de cada una (a,e,i,o,u)

a = 0
e = 0
i = 0
o = 0
u = 0
vocales = ["a","e","i","o","u"]

for j in range(len(vocales)):
    if vocales[j] == "a":
        a += 1
    elif vocales[j] == "e":
        e +=1
    elif vocales[j] == "i":
        i += 1
    elif vocales[j] == "o":
        o += 1
    elif vocales[j] == "u":
        u += 1
print("En total hay ",len(vocales),"vocales")
print("A:",a,"E:",e,"I:",i,"O:",o,"U:",u)