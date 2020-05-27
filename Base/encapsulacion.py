#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:14:55 2020

@author: luismanuelalvarez
"""


from numpy import hypot, sqrt

class Figura(object):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
        

class Rectangulo(Figura):
    def __init__(self, dim1, dim2):
    
        super(Rectangulo, self).__init__(dim1, dim2)
    
    def area(self):
        if self.dim1 != self.dim2:
            print('El area del rectangulo es ')
        else:
            print('El del cuadrado es ')
        return (self.dim1 * self.dim2)
    def perimetro(self):
        print('El perímetro del rectangulo es ')
        return(2 * self.dim1 + 2 * self.dim2)

class Triangulo(Figura):
    
    def __init__(self, dim1, dim2, base, altura):

        super(Triangulo, self).__init__(dim1, dim2)
        self.base = base
        self.altura = faltura
        
    def area(self):
        print('El area del Triángulo es ')
        return((self.base * self.altura) / 2.)
    def perimetro(self):
        print('El perímetro del Triángulo es ')
        return(self.dim1 + self.dim2 + self.base)
    def hipotenusa(self):
        print('La hipotenusa del Triángulo es ')
        return(hypot(self.base, self.altura))

    
    def main():
        F = Figura(5, 5)
        R = Rectangulo(6,5)
        print(R.area())
        print(R.perimetro())
    if __name__ == '__main__':
        main()
        