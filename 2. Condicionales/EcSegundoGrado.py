from math import *

a = float(input("Ingrese a: "))
b= float(input("Ingrese b: "))
c= float(input("Ingrese c: "))

# Calculo discriminante
d = b**2 - 4*a*c

if(d > 0):
    print("Raices reales y diferentes: ")
    x1 = (-b + sqrt(d))/2/a
    x2 = (-b - sqrt(d))/2/a
    print("X1: ", x1, "X2: ", x2)
if(d == 0 ):
    print("Raices Reales e Iguales: ")
    x1 = - b/2/a
    x2 = x1
    print("X1: ", x1, "X2: ", x2)
if(d < 0):
    print("Raices complejas y conjugadas: ")
    x1_real = -b/2/a
    x1_imagi = sqrt(-d)/2/a
    x2_real = -b/2/a
    x2_imagi = -1*sqrt(-d)/2/a

    print("x1 real: ", x1_real, "x1 imaginaria: ", x1_imagi)
    print("x2 real: ", x2_real, "x2 imaginaria: ", x2_imagi)

