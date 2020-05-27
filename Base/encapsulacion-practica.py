#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:16:42 2020

@author: luismanuelalvarez
"""


class Figura(object):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dm2 = dim2
    
class Rectangulo(Figura):
    def __init__(self, dim1, dim2):
        
        super(Rectangulo,self).__init__(dim1, dim2)
        
    
    def area(self):
        if self.dim1 != self.dim2:
            print('El area del rectangulo es ')
        else:
            print('El area del rectangulo es ')
        return (self.dim1 * self.dim2)
    
    def main():
        R = Rectangulo(5,4)
        print(R.area())

    if __name__ == '__main__':
        main()
        
        