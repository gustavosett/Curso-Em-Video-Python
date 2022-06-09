maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Diga o peso da {p}º pessoa!'))
    if p == 1:
        maior = peso           #aqui ele apenas define o primeiro peso.
        menor = peso
    else:
        if peso> maior:
            maior = peso       #aqui ele contabiliza para ver quem é o maior e quem é o menor.
        if peso< menor:
            menor = peso
print(f'O maior peso lido foi {maior}KG e o menor foi {menor}KG!')