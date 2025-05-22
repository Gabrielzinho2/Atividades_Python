funcionarios = {
    1: "Ana",
    2: "Carlos",
    3: "Maria",
    4: "Pedro"
}

print("Funcionarios atuais:  ")
for indice, nome in funcionarios.items():
    print(f"{indice}: {nome}")

numero_demissao = int(input("\nDigite o n° do funcionário a ser demitido:  "))

if numero_demissao in funcionarios:
    demitido = funcionarios.pop(numero_demissao)
    print(f"\nO funcionário {demitido} foi demitido!")

else:
    print("\nNumero de cadastro inválido!")

print("Funcioários restantes:  ")
for indice, nome in funcionarios.items():
    print(f"{indice}: {nome}")