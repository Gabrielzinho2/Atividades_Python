peso = float(input("\nPeso que João pescou(Kg): "))

if(peso>50):
    excesso = peso - 50
    multa = 4 * excesso
    print(f"\nTrouxe {excesso:,.2f}Kg acima do limite")
    print(f"\nSua multa por excesso foi de R${multa:,.2f}")

else: 
    print("Sem excedente. Não haverá multa")