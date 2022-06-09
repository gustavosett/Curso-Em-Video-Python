import random
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
numbers = random.randint(0, 5)
numero = (int(input('Em que número eu pensei? ')))
print('PROCESSANDO...')
if numero is numbers:
    print('Parabéns! você acertou!!!!')
else:
    print(f'Haha, parece que não! Meu número foi {numbers}!')