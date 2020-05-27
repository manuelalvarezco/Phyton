#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:36:54 2020

@author: luismanuelalvarez
"""


f = open('fichero','w')
f.write('fichero abirto en modo escritura\n')
f.write('por defecto se trata como un fichero de texto')
f.close()

for line in open('fichero'):
    print(line)
