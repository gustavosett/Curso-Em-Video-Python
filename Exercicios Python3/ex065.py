num = int(input('Digite um número: '))
cont = 1
soma = maior = menor = 0
resp = 'S'
while resp not in 'Nn':
    num = int(input('Digite outro número: '))
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    cont += 1
    resp = str(input('Você quer continuar? [S/N] '))[0].upper().strip()
    if resp != 'S' or resp != 'N':
        while resp not in 'SsNn':
            resp = str(input('Desculpa não entendi [S/N] '))[0].upper().strip()
print(f'Você digitou {cont} números e a média foi {(soma)/(cont)}!\n'
      f'O maior número foi {maior} e o menor foi {menor}!')
