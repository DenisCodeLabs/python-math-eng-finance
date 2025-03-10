from math import log

bandera = False
x = float(input("Dame el valor del numero x: "))
y = float(input("Dame el valor del numero y: "))

print("Dame la opcion que deseas realizar: \n")
print("1. Sumar (El primero mas el segundo)")
print("2. Restar (El primero menos el segundo)")
print("3. Multiplicar (El primero por el segundo)")
print("4. Dividir (El primero entre el segundo)")
print("5. Potencia (El primero elevado al segundo)")
print("6. Logaritmo (Logaritmo natural del primero)")

opcion = int(input("Ingresa la opcion: "))
if (opcion == 1):
    z = x+y
    print(x, "+", y)
elif(opcion == 2):
    z = x-y
    print(x, "-", y)
elif(opcion == 3):
    z = x*y
    print(x, "*", y)
elif(opcion == 4 and y != 0):
    z = x/y
    print(x, "/", y)
elif(opcion == 4 and y == 0):
    print("El denominador es igual a cero")
elif(opcion == 5):
    z = pow(x,y)
    print(x, "^", y)
elif(opcion == 6 and x > 0):
    z = log(x)
    print("ln(", x, ")")
elif(opcion == 6 and x <= 0):
    print("El valor de x es menor o igual a cero")
    bandera = True
else:
    print("Opcion invalida")

if (opcion < 7 and  bandera == False):
    print("Resultado: ", z)