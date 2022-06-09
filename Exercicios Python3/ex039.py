from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento? '))
idade = atual - nasc
print(f'Quem nasceu em {nasc}, tem ou terá {idade} anos em {atual}')
if idade == 18:
    print(f'Você tem que se alistar, imediatamente!')
elif idade < 18:
    print('Você ainda não precisa se alistar.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade-18} anos!')