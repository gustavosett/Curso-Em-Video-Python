from math import factorial
n = int(input('Digite um número: '))
c = n
print(f'Calculando fatorial de {n}! =', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else f' = {factorial(n)}', end='')
    c -= 1