cont = 1

while True:
    if cont == 1:
        n = int(input('\033[33mVeja a tabuada de: \033[m'))
    if n > 0:
        print(f'{n} x \033[33m{cont}\033[m = {n*cont}')
    cont += 1
    if cont == 11:
        cont = 1
    if n < 0:
        print('\033[32mObrigado e volte sempre!')
        break