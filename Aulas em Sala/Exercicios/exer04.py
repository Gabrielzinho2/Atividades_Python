lista1 = [1,4,6]
lista2 = [2,4,3]

lista_resultante = []

for i in range(3):
    soma = lista1[i] + lista2[i]
    lista_resultante.append(soma)

print(f"Lista resultante: {lista_resultante}")