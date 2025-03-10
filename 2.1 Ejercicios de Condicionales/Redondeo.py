from math import *

number =input("Ingrese un número: ")
if(number.__contains__(".")):
    print(floor(float(number)))
else:
    print("El numero ", number, " es entero")
