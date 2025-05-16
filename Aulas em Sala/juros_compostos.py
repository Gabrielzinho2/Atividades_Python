pv = float(input("Digite o valor do investimento inicial: "))

i = float(input("Digite o valor da taxa em (%): "))

n = int(input("Digite  número de meses que o dinheiro ficará aplicao: "))

print("O valor da taxa percentual é de :",i)

i = (i/100);

print("O valor da taxa decimal é de: ",i)

fv = pv * ((1+i)**n)

print("O montante da aplicação será de R$",fv)
