#from src.calculator import mysum,divide
#import src.calculator as clc
from src.calculator import *
class FooCalculator:
    def __init__(self):
        pass

    def somma(self,m,n):
        return mysum(m,n)

    def divisione(self,m,n):
        return divide(m,n)

    def subtract(self,m,n):
        return subtract(m,n)

    def multiply(self,m,n):
        return multiply(m,n)

test=FooCalculator()
a=-9
b=-2
print("test.sum->",a,"+",b,"=",test.somma(a,b))
a=-21
b=3
print("test.divide->",a,":",b,"=",test.divisione(a,b))

a=-21
b=3
print("test.subtract->",a,"-",b,"=", test.subtract(a,b))

a=-21
b=3
print("test.multiply->",a,"*",b,"=", test.multiply(a,b))