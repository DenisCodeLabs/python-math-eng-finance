
opcion = input("Ingresa una opción: \n1. Radianes a grados\n2. Grados a radianes\n: ")

if(opcion == "1"):
    radianes = float(input("Ingresa los radianes: "))
    print("Grados: ", radianes * 180 / 3.1416)
elif(opcion == "2"):
    grados = float(input("Ingresa los grados: "))
    print("Radianes: ", grados * 3.1416 / 180)
else:
    print("Opción no válida")