from random import choice
listanum = []
while True:
    valor = int(input('Digite um valor: '))
    listanum.append(valor)
    while True:
        resp = str(input('Quer continuar?[S/N] '))[0].upper()
        if resp == 'S' or resp == 'N':
            break
        else:
            print('Desculpa, não entendi!')
    if resp == 'N':
        break
print(f'Você digitou {len(listanum)} elementos\n'
      f'Os valores decrecentes são {sorted(listanum)[::-1]}\n'
      f'O valor aleatório {choice(listanum)} faz parte da lista!')
if 5 in listanum:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'Não tem o valor 5 na lista!')