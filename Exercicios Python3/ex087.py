matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for a in range(0, 3):
        matriz[c][a] = int(input(f'Digite o valor para {a}, {c}: '))

for c in range(0, 3):
    for a in range(0, 3):
        print(f'[{matriz[c][a]:^5}]', end='')
    print()

par = tc = mv = 0
for c in range(0,3):
    tc += matriz[c][2]
    if c == 0:
        mv = matriz[c][1]
    else:
        if mv < matriz[c][1]:
            mv = matriz[c][1]
    for l in range(0,3):
        if matriz[c][l] % 2 == 0:
            par += matriz[c][l]

print(f'A soma dos valores pares é {par}\n'
      f'A soma dos valores da terceira coluna é {tc}\n'
      f'O maior valor da segunda coluna é {mv}')