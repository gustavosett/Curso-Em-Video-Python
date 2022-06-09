cor = {'limpa':'\033[m',
       'azul':'\033[34m',
       'ciano':'\033[36m'}
n = int(input(f'{cor["azul"]}Digite um número.{cor["limpa"]} '))
s = n+1
a = n-1
print(f'{cor["ciano"]}O sucessor de {n} é {s} e seu antecessor é {a}{cor["limpa"]}!')