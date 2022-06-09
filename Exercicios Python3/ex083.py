conta = str(input('Digite sua expressão: '))

cont = 0

for x in conta:
    if x == '(':
        cont += 1
    if x == ')':
        cont -= 1
    if cont < 0:
        print('Conta inválida!')
        exit(0)
if cont != 0:
    print('Conta inválida!')
else:
    print('Conta válida!')