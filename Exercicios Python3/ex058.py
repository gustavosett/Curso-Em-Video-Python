from random import randint
escolha_ia = randint(1, 10) #escolha do computador
print('-'*5,'JOGO DO ADIVINHA','-'*5)
print('Sou seu computador e pensei em um número de 1 a 10!')
escolha_jogador = int(input('Tente adivinhar o número: '))
cont = 1
if escolha_jogador != escolha_ia:
    while escolha_jogador != escolha_ia:
        escolha_jogador = int(input('Errou! Tente novamente: '))
        cont += 1
print(f'Parabéns o computador pensou no {escolha_ia}'
        f' e você acertou em {cont} tentativas!!!')