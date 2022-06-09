def ficha(jg , gol):
    print(f'O jogador {jg}, fez {gol} gols!')


jogador = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if not jogador.isalpha():
    jogador = '<desconhecido>'
ficha(jogador, gols)