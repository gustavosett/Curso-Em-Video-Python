def LeiaInt(a):
    b = str(input(a))
    if b.isnumeric():
        return b
    else:
        print('Você não digitou um número!')
        return 'nenhum'

while True:
    n = LeiaInt('Digite um número: ')
    if n.isnumeric():
        print(f'Você acabou de digitar o número: {n}')
        break