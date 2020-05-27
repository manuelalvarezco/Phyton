#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:16:54 2020

@author: luismanuelalvarez
"""


class Estudiante:
    def __init__(self,nombre,edad=16):
        
        self.nombre = nombre
        self.edad = edad
    
    def devuelve_datos(self):
        
        if(self.edad > 18):
            return "El estudiante"+ self.nombre + " con edad "+ str(self.edad) +" es mayor de edad"
        
        return "El estudiante " + self.nombre + " Es menor de edad"

if __name__ == '__main__':
    
    a1 = Estudiante('Manuel', 30)
    print(a1.devuelve_datos())