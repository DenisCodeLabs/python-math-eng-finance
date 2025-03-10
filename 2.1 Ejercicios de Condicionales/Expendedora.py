
moneda = int(input("Introduce una moneda de $5, $10: \n"))
cantidad = int(input("Introduce la cantidad de dulces ($2 C/U): "))	
if(moneda == 5 or moneda == 10):
    if(moneda < (cantidad * 2)):
        print("Credito insuficiente")
    elif(moneda > (cantidad * 2)):
        print("Su cambio es: ", moneda - (cantidad * 2))

else:
    print("Moneda no válida")