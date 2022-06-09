from random import randint
from time import sleep
from operator import itemgetter
dado = dict()
for c in range(1, 5):
    dado[f'jogador{c}'] = f'{randint(1, 6)}'
ranking = list()
for k, v in dado.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.7)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('=-'*15)
print(f'{"== RANKING DOS JOGADORES ==":^2}')
lugar = 1
for k, v in enumerate(ranking):
    sleep(1)
    print(f'{lugar}º lugar: {v[0]} com {v[1]}')
    lugar += 1