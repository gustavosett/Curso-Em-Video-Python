from random import randint
nuu = int(input('Você quer quantos números aleatórios?[0/10] '))
tupla = tuple(randint(0, 9) for i in range(nuu))
print(f'Os valores sorteados foram: {str(tupla).replace("(" or ")", "")}')
print(f'O numero maior foi {max(tupla)} e o menor foi {min(tupla)}!')