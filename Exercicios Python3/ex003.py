cor = {'azul':'\033[34m',
       'rosa':'\033[95m',
       'ciano':'\033[36m',
       'limpa':'\033[m'}
n1=int(input(f'{cor["azul"]}Digite um número: {cor["limpa"]}'))
n2=int(input(f'{cor["ciano"]}Digite outro número: {cor["limpa"]}'))
s=n1+n2
print(f'{cor["rosa"]}A soma de {n1} mais {n2} é {s}{cor["limpa"]}')