from datetime import datetime


def voto(ano):
    dia = datetime.today().year
    idade = dia - ano
    return idade


idade = voto(int(input('Em que ano você nasceu?')))

if idade > 18:
    print(f'Com {idade} anos, é obrigado a votar!')
elif 18 > idade >= 16 or idade > 65:
    print(f'Com {idade} anos, pode votar, mas não é obrigatório!')
else:
    print(f'Com {idade} anos, não pode votar!')
