max_speed = float(input("Qual a velocidade máxima da via (Km/h): "))

speed = float(input("Qual velocidade o motorista estava (Km/h): "))

diferenca = max_speed - speed

if (diferenca >= 0) :
    print("\nVel. normal")
elif (diferenca >= -10) :
    print("\nMulta de R$85,13")
    print("\nInfração leve  -  3 pontos na carteira")
elif (diferenca >= -30) :
    print("\nMulta de R$127,69")
    print("\nInfração média  -  5 pontos na carteira")
else :
    print("\nMulta de R$574.62")
    print("\nInfração grave  -  7 pontos na carteira")