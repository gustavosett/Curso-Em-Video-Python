listanum = []
listapar = []
listaimpar = []
while True:
    listanum.append(int(input('Digite um número: ')))
    while True:
         resp = str(input('Quer continuar?[S/N] '))[0].upper()
         if resp == 'N':
             break
         elif resp == 'S':
             break
         else:
             print('Desculpa não entendi!')
    if resp == 'N': break
for i, v in enumerate(listanum):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'A lista completa é {listanum}\n'
      f'A lista de pares é {listapar}\n'
      f'E a lista de impares é {listaimpar}')

# while True:
#     num = int(input('Digite um número: '))
#     listanum.append(num)
#     if num % 2 == 0:
#         listapar.append(num)
#     else:
#         listaimpar.append(num)
#     while True:
#         resp = str(input('Quer continuar?[S/N] '))[0].upper()
#         if resp == 'N':
#             break
#         elif resp == 'S':
#             break
#         else:
#             print('Desculpa não entendi!')
#     if resp == 'N': break
# print(f'A lista completa é {listanum}\n'
#       f'A lista de pares é {listapar}\n'
#       f'E a lista de impares é {listaimpar}')
