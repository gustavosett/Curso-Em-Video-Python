jogador = dict()
jogadorl = list()
partida = list()
while True:
    jogador["nome"] = str(input('Nome do jogador: '))
    partidas = int(input('Partidas: '))
    for p in range(0, partidas):
        jogadorl.append(int(input(f'Quantos gols na partida {p+1}?')))
    jogador["gols"] = jogadorl[:]
    jogador["total"] = sum(jogadorl)
    partida.append(jogador.copy())
    jogadorl.clear()
    while True:
        resp = str(input("Quer continuar?[S/N]"))[0].upper()
        if resp == "S" or resp == "N":
            break
        else:
            print("Por favor, apenas S ou N!")
    if resp == "N": break
print('-='*20)
print(f'{"cod":<5}{"nome":<15}{"gols":<15}{"total"}')
print('-'*25)
for i, v in enumerate(partida):
    print(f'{i:<5}{v["nome"]:<15}{v["gols"]}{v["total"]:>8}')