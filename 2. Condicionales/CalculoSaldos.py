print("Dame el saldo actual")
Saldo = float(input())

if(Saldo < 10000.00):
    Saldo *= (1+0.03)
else:    
    Saldo *= (1+0.04)
print("Saldo Final: %.2f" %Saldo)
