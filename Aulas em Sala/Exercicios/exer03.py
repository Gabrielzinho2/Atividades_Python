x = int(input("Digite o valor de x:  "))
y = int(input("Digite o valor de y:  "))

if x < y:
    resultado = list(range(x,y+1))

    print(f"Os valores entre {x} e {y} (inclusive) são: {resultado}")

else:
    print(f"Erro: O valor de x deve ser menor que o valor de y!")