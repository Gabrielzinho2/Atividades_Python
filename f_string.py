premio = float(input("Digite o valor do prêmio: "))
ganhadores = int(input("Digite número de ganhadores: "))

print(f"\nO prêmio foi de R$ {premio:,.2f}, com {ganhadores} ganhadores e receberam R$ {premio/ganhadores:,.2f} cada")