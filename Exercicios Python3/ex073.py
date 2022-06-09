times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Vasco', 'Chapecoense','Atlético-PR', 'Bahia', 'Sport Recife',
         'Avai', 'Ponte Preta','Cruzeiro', 'Flamengo','Atlético', 'Botafogo','São Paulo', 'EC Vitória', 'Coritiba',
         'Atlético-G0','Fluminense')
print('-=' * 15)
print(f'Lista de times do Brasileirão:\n {", ".join(times)}')
print('-=' * 15)
print(f'0s 5 primeiros são: {", ".join(times[:5])}')
print('-' * 15)
print(f'0s 4 últimos são: {", ".join(times[-4:len(times)])}')
print('-' * 15)
print(f'Times em ordem alfabética:\n {", ".join(sorted(times))}')
print('-' * 15)
print(f'Chapecoense está na posição: {times.index("Chapecoense")+1}º lugar')