valor = int(input("Entre com o valor a ser sacado: "))

notas = (100, 50, 20, 10, 5, 1)

for i in range(0, len(notas)):
    quantidade = int(valor / notas[i])
    valor = valor % notas[i]
    print(f"Entregar {quantidade} nota(s) de {notas[i]}")