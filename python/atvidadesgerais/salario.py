salBase = float(input('Informe salário: '))
grat = float(input("Informe a gratificação (apenas o número da porcentagem): "))
newgrat = salBase * (grat / 100)
salRebecer = salBase + newgrat
imp = salRebecer * 7 / 100
salRebecer = salRebecer - imp
print(f'O salário a receber após impostos é: R${salRebecer:.2f}')