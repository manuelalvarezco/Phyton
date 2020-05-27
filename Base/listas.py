#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:48:42 2020

@author: luismanuelalvarez
"""


lista = ['1','2','3']

#for num in lista:
#   print(num)

print(lista.reverse())



#Iterador
iterator = (['python','Java','C++'])
print(iterator)
for element in iterator:
    print(element)
    
    
#Diccionario
diccionario = {'ip':'192.1.1.0','port':'8080','state':'open'}

claves=diccionario.keys()
valores = diccionario.values()

for clave,valor in diccionario.items():
    print(clave, '->', valor)
    

diccionario = {'ip':'192.1.1.0','port':'8080','state':'open'}

del(diccionario['state'])

diccionario.clear()

print(diccionario)