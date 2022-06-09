jogador = dict()
jogadorl = list()
jogador["nome"] = str(input('Nome do jogador: '))
partidas = int(input('Partidas: '))
for p in range(0, partidas):
    jogadorl.append(int(input(f'Quantos gols na partida {p+1}?')))
jogador["gols"] = jogadorl
jogador["total"] = sum(jogadorl)
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(jogador["gols"]):
    print(f'Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols!')