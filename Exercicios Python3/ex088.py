import random
import time
jg = int(input('Quantos jogos você quer que eu sorteie? '))
jogo = list()
lista = list()
for j in range (0, jg):
    for o in range(0,6):
        while True:
            num = random.randint(1, 60)
            if num not in jogo:
                jogo.append(num)
                break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
for p in range (0, jg):
    print(f'Jogo {p+1}: {lista[p]}')
    time.sleep(1)