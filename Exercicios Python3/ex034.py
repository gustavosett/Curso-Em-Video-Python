salario = int(input('Qual o salário do funcionário? '))
if salario > 3000:
    print(f'Quem ganhava R${salario}, agora vai ganhar um aumento de R${((salario/100)*10)}!')
else:
    print(f'Quem ganhava R${salario}, agora vai ganhar um aumento de R${((salario/100)*15)}')