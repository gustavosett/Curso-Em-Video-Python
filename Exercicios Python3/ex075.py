num =  (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite outro número: ')))
print(f'Você digitou os valores {num}')
print(f'O maior valor {max(num)} apareceu {num.count(max(num))} vezes') #desnecessauro
print(f'O menor valor {min(num)} apareceu na {num.index(min(num))+1}ª posição')
contador = 0
for c in range(0, 4):
    if num[c] % 2 == 0:
        contador += 1
print(f'{contador} desses números são pares')