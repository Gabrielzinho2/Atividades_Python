import math

n1 = int(input("\nDigite o primeiro número:  "))
n2 = int(input("\nDigite o segundo número:  "))
n3 = int(input("\nDigite o terceiro número:  "))

maior = max(n1, n2, n3)

menor = min(n1, n2, n3)

print(f"\nO menor número é {menor}")

print(f"\nO maior número é {maior}")