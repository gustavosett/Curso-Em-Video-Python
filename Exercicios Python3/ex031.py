km = int(input('Qual é a distancia da sua viagem? '))
if km < 200:
    print(f'Você está prestes a comprar uma passagem de {km} km!')
    print(f'O preço da sua passagem será de R$ {km/2:.2f}')
else:
    print(f'Você está prestes a comprar uma passagem de {km} km!')
    print(f'O preço da sua passagem será de R$ {km*0.45:.2f} e vai economizar R$ {(km/2)-(km*0.45):.2f}!')