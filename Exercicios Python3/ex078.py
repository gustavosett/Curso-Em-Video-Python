lista = []
for p in range(1, 5):
    lista.append(int(input(f'Digite o {p}º número: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if lista[i] == (max(lista)):
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if lista[i] == (min(lista)):
        print(f'{i}...', end='')