sal_base   = 1500
comissao   = 200

corretor   = input("nome: ")
qtd_vendas = int(input("quantidade de imóveis vendidos: "))
tot_vendas = float(input("valor total das vendas do corretor: "))

sal_final  = sal_base + comissao * qtd_vendas + tot_vendas * 0.05

print(f"Salário final de {corretor} é R$ {sal_final:.2f}")