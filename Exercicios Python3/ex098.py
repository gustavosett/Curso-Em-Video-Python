from time import sleep
def contador(a, b, c):
    if c < 0:
        c = c * -1
    elif c == 0:
        c = 1
    print('~'* 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2)
    if a > b:
        cont = a
        while cont >= b:
            print(f'{cont}..', end='')
            cont -= c
            sleep(0.3)
    else:
        cont = a
        while cont <= b:
            print(f'{cont}..', end='')
            cont += c
            sleep(0.3)
    print()


contador(1, 10, 1)
contador(10, 0, 2)

inic = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(inic, fim, pas)