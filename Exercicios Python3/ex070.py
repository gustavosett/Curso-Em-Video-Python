cont = maiorp = tot = maisd1000 = 0
nomemaiorp = resp = 'fodase'
while True:
    if cont >= 1:
        while True:
            resp = str(input('Quer continuar?[Sim/Não] '))[0].upper()
            if resp == 'S':
                break
            elif resp == 'N':
                break
            else:
                print('Desculpa não entendi!')
    if resp == 'N':
        break
    ndp = str(input('Nome do produto: '))
    pdp = float(input('Preço do produto: '))
    if cont == 0:
        maiorp = pdp
        nomemaiorp = ndp
    else:
        if pdp > maiorp:
            maiorp = pdp
            nomemaiorp = ndp
    if pdp > 1000:
        maisd1000 += 1
    tot += pdp
    cont += 1
print(f'Total gasto foi R$ {tot}\n'
      f'{maisd1000} produtos foram mais de R$1000.00!\n'
      f'O produto mais caro foi {nomemaiorp}!')