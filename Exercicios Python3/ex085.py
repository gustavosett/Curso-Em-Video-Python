numl = [[], []]
for n in range(0, 7):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 ==0:
        numl[0].append(num)
    else:
        numl[1].append(num)
print(f'Aqui está a lista de pares: {numl[0]}\n'
      f'E de impares: {numl[1]}')