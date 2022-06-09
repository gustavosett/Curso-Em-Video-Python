print('Gerador de PA')
print('-='*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite e razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')