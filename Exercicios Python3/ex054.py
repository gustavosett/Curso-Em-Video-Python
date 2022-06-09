from datetime import date
hoje = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    pessoa = int(input('Ano de nascimento: '))
    idade = hoje - pessoa
    if idade >= 18:
        print('\033[32mEssa pessoa é de maior!\033[m')
        totalmaior += 1
    else:
        print('\033[31mEssa pessoa é de menor!\033[m')
        totalmenor += 1
print(f'Foi um total de \033[32m{totalmaior} maiores de idade\033[m e \033[31m{totalmenor} menores de idade\033[m!')