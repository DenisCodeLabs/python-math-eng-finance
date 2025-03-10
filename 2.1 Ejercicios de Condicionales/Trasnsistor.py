""" 
Algoritmo que calcula el valor  de Id para el valor que se recibe de Vds. Usar los valores de Vds = 0.5  y 1
Vgs = 0.2, 0.5, 1.0
"""
# Constans
k = 0.0025
Vt = 0.025
Vgs = 0.2

Vds = float(input("Ingrese el valor de Vds: "))
if((Vgs -Vt) <= Vds):
    Id = k * (Vgs - Vt) ** 2


elif((Vgs -Vt) > Vds):
    Id = k *(2(Vgs - Vt) * Vds - Vds ** 2)

print("El valor de Id es: %.10f" %Id)