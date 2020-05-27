#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:19:34 2020

@author: luismanuelalvarez
"""


#try:
#    a = 1/0
#except:
#    print('Exception division by cero')

try:
    lista = ['1','2','3']
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(lista[100])
except:
    print('Fuera de rango')
