from ex109 import moeda
num = float(input('Digite um preço: R$'))
print(f'Metade de {num}, é R${moeda.metade(num)}')
print(f'O dobro de {num}, é R${moeda.dobro(num)}')
print(f'Somando 10% é R${moeda.porcen(num)}')
