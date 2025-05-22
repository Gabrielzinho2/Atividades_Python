peso = float(input("\nInforme o peso da carga(Kg): "))

km = float(input("\nInforme a distância do transporte(Km): "))

tipo = int(input("\nInforme o tipo da carga (1 -- comum, 2 -- perecível): "))

seguro = input("\nO transporte é com seguro? (S -- sim, N -- não): ")

custo_base = 0.50 * km * peso

if(tipo == 1):
    if(seguro == "S"):
        custo_final = custo_base + 50
        print(f"O valor base é de R${custo_base:,.2f}")
        print(f"O valor a pagar com seguro é de R${custo_final:,.2f}")
    elif(seguro == "N"):
        custo_final = custo_base
        print(f"O valor base é de R${custo_base:,.2f}")
        print(f"O valor a pagar sem seguro é de R${custo_final:,.2f}")

        
elif(tipo == 2):
    if(seguro == "S"):
        custo_final = custo_base + ((custo_base * 20 )/ 100)
        final_seguro = custo_final + 50
        print(f"O valor base é de R${custo_base:,.2f}")
        print(f"O valor com acréscimo de tipo é de R${custo_final:,.2f}")
        print(f"O valor a pagar com seguro é de R${custo_final:,.2f}")
    elif(seguro == "N"):
        custo_final = custo_base + ((custo_base * 20 )/ 100)
        print(f"O valor base é de R${custo_base:,.2f}")
        print(f"O valor com acréscimo de tipo é de R${custo_final:,.2f}")
        print(f"O valor a pagar sem seguro é de R${custo_final:,.2f}")
