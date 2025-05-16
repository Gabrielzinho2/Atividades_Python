medias = []

for i in range(10): 
    print(f"\nDigite as 4 notas do {i + 1} aluno: ")

    soma_notas = 0
    for j in range(4): 
        nota = float(input(f"Digite a {i + 1} nota: "))
        soma_notas += nota

    media = soma_notas/4
    medias.append(media)

alunos_aprovados = 0
for n in medias: 
    if n >= 7:
        alunos_aprovados += 1

print(f"\nNúmero de alunos com média maior ou igual a 7: {alunos_aprovados}")