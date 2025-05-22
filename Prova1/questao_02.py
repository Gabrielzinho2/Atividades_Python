consumo = 0.8

valor = 0.85

tempo = int(input("\nDigite quantas horas o aparelho é usado: "))

consumo_total = consumo * tempo

valor_pagar = consumo_total * valor

print(f"\nO consumo total de energia foi de {consumo_total:,.2f}kWh")

print(f"\nO valor a se pagar pelo uso do equipamento é de R${valor_pagar:,.2f}")
