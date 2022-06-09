import random
def sorteia(lista):
    sort = random.randint(1, 10)
    for i in range(0, sort):
        num = random.randint(0, sort)
        lista.append(num)
    print(f'Sorteando {sort} valores da lista: {lista}')

def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma de todos números pares é {soma}')

numero = list()
sorteia(numero)
somapar(numero)