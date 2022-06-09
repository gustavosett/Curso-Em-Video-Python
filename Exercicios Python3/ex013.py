salario = float(input('Diga seu salário e ganhe já 15% de aumento! '))
aumento = (salario/100)*15
sca = salario+aumento
print(f'Parabéns, apartir de hoje de R${salario},',end=' '
f'você ganhará R${sca:.2f}!!! Totalizando um ganho de R${aumento:.2f}!!')
