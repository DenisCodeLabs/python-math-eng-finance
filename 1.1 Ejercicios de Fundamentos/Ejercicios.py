'''
¿Cual es la salida del algoritmo que esta acontinuacion?
'''
n = 4; k = 2
print(n)
print(-n)
#print(n-)
print(n + k)
print(k)
print(n, k)
print("")
print("n%3.2g" %n)
print(" n * n = %3.2g"%(n*n))
print(n*n)
print(' n')

'''
Indique cual es la salida en los siguientes segmentos
'''
# a)
x = 3
x = x + 2
print(x)

# b)
y = -5.3
y = y*7.0
print(y)

# c)
import math

x = 8
y = 3
x = math.fmod(x, y)
print(x)

'''
La funcion getsizeof() se usa para calcular el tamanio de una variable en bytes. Calcule el tamanio de la variable 'a' con getsizeof()
'''
import sys

a = 2.0
print(sys.getsizeof(a))

a = 2
print(sys.getsizeof(a))

a = 20000
print(sys.getsizeof(a))

a = '2'
print(sys.getsizeof(a))

a = True
print(sys.getsizeof(a))

'''
Indique que resultado produce el siguiente copdigo
'''	

x = 42.0
y = 42.3e-14
a = 42.3e-14
b = -57.8
m = +87
n = +249
print(m*n)
print(x)
print(y)
print(a)
print(b)

'''
Indique el resultado que produce el siguiente codigo
'''

# a)
x = 90.34;
print(x)

# b)
z = 2
y = 7
x = y + 2*z
print("El resultado es: %5.2g" %x)

'''
Cual es el resultado, Verdadero o Falso, 1 o 0, que se produce en el siguiente codigo por inspeccion y luego compruebe en la computadora
'''
x = 8; y =5
a = 1; b = 2

# a)
print((x == 1) & (a <= 2) | (y < x))

# b)
print(((x == 1) & (a <= 2)) | (y > x))

# c)
print(x == 1 & (a <= 2 | y ==x))

'''
Escriba el resultado que se obtiene en el siguiente codigo
'''
a = 2; b = 3
x = 8.3; y = -4.6; z = 2.3
print("a*b =%5.2f" %a*b)
print("a/b =%5.2f" %(a/b))
print("x/y =%5.2f" %(x/y))
print("a*z =%5.2f" %(a*z))

'''
Escriba el resultado que se produce
'''

c ='8'
x = 3
print(c*x)

'''
Escriba un algoritmo que lea los datos: 7,2,8.3, 3,5.6,4 y calcule lo siguiente:
el mayor
el menor
la suma
la media
'''

a = 7; b = 2; c = 8.3; d = 3; e = 5.6; f = 4
mayor = max(a,b,c,d,e,f)
menor = min(a,b,c,d,e,f)
suma = a + b + c + d + e + f
media = suma / 6
print("El mayor es: ", mayor)
print("El menor es: ", menor)
print("La suma es: ", suma)
print("La media es: ", media)