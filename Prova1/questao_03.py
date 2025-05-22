ingresso = input("\nEscolha o tipo do seu ingresso (comum ou VIP):")

pagamento = input("\nDefina o método de pagamento(pix ou cartão):")

qtd_ingressos = int(input("\nDefina a quantidade de ingressos: "))

vip = 50

comum = 30

valor_vip = 50 * qtd_ingressos

valor_comum = 30 * qtd_ingressos


if (ingresso == "comum"):
	if (pagamento == "cartao"):
		print(f"O total a pagar é de R${valor_comum:,.2f}")
	else:
		valor_final = valor_comum - (valor_comum * 15 / 100)
		print(f"O total a se pagar é de R${valor_final}")


elif (ingresso == "vip"):
        if (pagamento == "cartao"):
                print(f"O total a pagar é de R${valor_vip:,.2f}")
        else:
                valor_final = valor_vip - (valor_vip * 15 / 100)
                print(f"O total a se pagar é de R${valor_final}")
	
