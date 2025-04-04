num1 = int(input("Digite o número:  "))
num2 = int(input("Digite o número:  "))
num3 = int(input("Digite o número:  "))

maior = 0
menor = 9999999

if (num1 > maior and num1 > num2 and num1 > num3):
    maior = num1

elif (num2 > maior and num2 > num1 and num2 > num3):
      maior = num2

elif (num3 > maior and num3 > num1 and num3 > num2):
    maior = num3

print(f"\nO maior número é {maior}")

if (num1 < menor and num1 < num2 and num1 < num3):
    menor = num1

elif (num2 < menor and num2 < num1 and num2 < num3):
      menor = num2

elif (num3 < menor and num3 < num1 and num3 < num2):
    menor = num3

print(f"\nO menor número é {menor}")