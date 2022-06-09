from random import choice
from os import system

palavras = ['processador', 'memoria', 'fonte', 'gabinete',
            'cooler', 'monitor', 'teclado', 'headset']
palavra = list(choice(palavras))
palavrasubli = list('_' * len(palavra))
cont_derrotas = 0


def acertou(resp):
    inicio = -1
    for i in range(0, palavra.count(resp)):
        numresp = palavra.index(resp, inicio + 1)
        palavrasubli[numresp] = resp
        inicio = numresp


while True:  # jogo
    print(''.join(palavrasubli))
    while True:
        try:
            resp = str(input('\ntente uma letra: '))[0]
            break
        except:
            print('por favor digite um caractere válido.')
    if resp in palavra:
        acertou(resp)
    else:
        print('errou.')
        cont_derrotas += 1

    if cont_derrotas == 10:
        print(f'você perdeu! a palavra é: {"".join(palavra)}')

    elif palavrasubli == palavra:
        print(f'parabéns vc ganhou!'
              f' a palavra é: {"".join(palavra)}')
        break
