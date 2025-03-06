'''
Calculo de interes simple y compuesto
'''

Capital = float(input("Introduce el capital inicial: "))
Tasa = float(input("Introduce la tasa de interes: "))
Tiempo = float(input("Introduce el tiempo en meses: "))

Isimple = (Capital * Tasa * Tiempo)
ICompuesto = Capital * (1 + Tasa) ** Tiempo

print("El interes simple es: ", Isimple)
print("El interes compuesto es: ", ICompuesto)
