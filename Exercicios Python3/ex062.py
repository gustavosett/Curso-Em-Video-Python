print('Gerador de PA')
print('-='*20)
cont = 0
termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
perg = 10
while perg != 0:
    for c in range(0, perg):
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    perg = int(input('\n\033[33mQuantos termos você quer mostrar '
                     'a mais?\033[m[digite 0 para cancelar] '))
print(f'Sua progressão foi finalizada com '
      f'\033[33m{cont}\033[m termos mostrados')