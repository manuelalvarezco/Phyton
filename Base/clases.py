#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:44:36 2020

@author: luismanuelalvarez
"""


class Prueba:
    def __init__(self, x=2):
        
        self.x = x
        self.y = x**2
    def devuelve_valor(self):
    
        return "Con x=%i obtenemos: y=%i" % (self.x, self.y)
if __name__ == '__main__':
    
    a1 = Prueba(2)
    print(a1.devuelve_valor())
    
    a2= Prueba(3)
    print(a2.devuelve_valor())

