x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
z = int(input('Digite o terceiro valor: '))
menor = x
if y<x and y<z:
    menor = y
if z<x and z<y:
    menor = z
maior = x
if y>x and y>z:
    maior = y
if z>x and z>y:
    maior = z
print(f'O maior número é {maior}\ne o menor é {menor}!')