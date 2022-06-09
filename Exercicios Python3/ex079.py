listanum = []
listanum.append(int(input('Digite um número: ')))
while True:
    num = int(input('Digite outro número: '))
    if num in listanum:
        print('Número igual, não vou adicionar!')
    elif num not in listanum:
        listanum.append(num)
        while True:
            resp = str(input('Quer continuar?[S/N] '))[0].upper()
            if resp == 'S':
                break
            elif resp == 'N':
                break
            else:
                print('Não entendi.')
        if resp == 'N':
            break
print(f'Você digitou os valores {sorted(listanum)}')