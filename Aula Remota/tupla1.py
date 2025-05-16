valor = int(input("Digite o valor a ser sacado: "))

notas(100,50,20,10,5)

notas100 = int(valor/notas[0])
valor = valor % 100
print("Entregar ",notas100 ," nota(s) de ", notas[0])

notas50 = int(valor/notas[1])
valor = valor % 50
print("Entregar ",notas50 ," nota(s) de ", notas[1])

notas20 = int(valor/notas[2])
valor = valor % 20
print("Entregar ",notas20 ," nota(s) de ", notas[2])

notas10 = int(valor/notas[3])
valor = valor % 10 
print("Entregar ",notas10 ," nota(s) de ", notas[3])

nota5 = int(valor/notas[4])
valor = valor % 5
print("Entregar ",nota5 ," nota(s) de ", notas[4])