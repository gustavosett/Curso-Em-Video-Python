cont = 1
resp = 'fodase'
mais18 = homemc = mulherm20 = 0
while True:
    if cont > 1:
        while True:
            resp = str(input('Quer continuar?[Sim/Não] ')).upper()
            if resp == 'NÃO':
                break
            elif resp == 'SIM':
                break
            else:
                print('Desculpa não entendi!')
    if resp == 'NÃO':
        break
    nome = str(input(f'Qual o nome da {cont}ª pessoa: '))
    idade = int(input(f'Diga a idade de {nome}: '))
    sexo = str(input('Qual o sexo?[M/F] '))[0].upper()
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homemc += 1
    if sexo == 'F' and idade < 20:
        mulherm20 += 1
    cont += 1
print(f'Ao total tem {mais18} pessoas maiores de 18 anos.\n'
      f'Foram {homemc} homens cadastrados,\n'
      f'e {mulherm20} mulheres tem menos de 20 anos!')