s = 0
for c in range(1, 7):
    n = int(input(f'{c}º número: '))
    s += n
if (s%2) == 0:
    print(f'{s} é um número par!')
else:
    print(f'{s} é um número impar!')