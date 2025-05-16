vetor1 = []
vetor2 = []

print("Digite os 5 elementos do primeiro vetor :")
for i in range(5):
    elemento = input(f"Digite o {i + 1} elemento do vetor 1: ")
    vetor1.append(elemento)

print("\nDigite os 5 elementos do segundo vetor :")
for i in range(5):
    elemento = input(f"Digite o {i + 1} elemento do vetor 2: ")
    vetor2.append(elemento)

vetor_intercalado = []
for j in range(5):
    vetor_intercalado.append(vetor1[j])
    vetor_intercalado.append(vetor2[j])

print("\nVetor1: ",vetor1)
print("\nVetor2: ",vetor2)
print("\nVetor intercalado: ",vetor_intercalado)