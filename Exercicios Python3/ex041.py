from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

if idade > 20:
    print('Classificação: SÊNIOR')
elif idade <= 20 and idade >= 16:
    print('Classificação: JUNIOR')
else:
    print('Classificação: MIRIM')