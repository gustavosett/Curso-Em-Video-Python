nota1 = float(input('Nota na primeira prova: '))
nota2 = float(input('Nota na segunda prova: '))
media = (nota1 + nota2) /2
if media < 5.0:
    print(f'Sinto muito, você foi reprovado com média de {media:.2f} pontos!')
elif media > 5.0 and media < 7:
    print(f'Você está de recumeração com média de {media}, você precisará de {(7 - media):.2f} ponto(s)!')
elif media == 10:
    print(f'Caraca, você passou com nota máxima 10!!!')
else:
    print(f'Parabéns você passou direto com uma média de {media} pontos!')