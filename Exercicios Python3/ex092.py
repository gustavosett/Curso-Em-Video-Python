import datetime
from datetime import date
data = date.today().year
trabalhador = dict()

trabalhador["nome"] = str(input('Nome: '))
trabalhador["idade"] = data - int(input('Ano de nascimento: '))
trabalhador["ctps"] = int(input('Carteira de Trabalho[0 não tem]: '))
if trabalhador["ctps"] != 0:
    trabalhador["emprego"] = int(input('Ano de Contratação: '))
    trabalhador["salário"] = float(input('Salário: R$'))
    trabalhador["aposentadoria"] = (trabalhador["idade"] + 35) - (data - trabalhador["emprego"])

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')