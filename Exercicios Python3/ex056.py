maioridade = 0
total = 0
mu = 0
nomemais = 'NENHUM HOMEM'

for i in range(1,5):
    print('-'*5,f'{i}ª PESSOA','-'*5)
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).upper()
    if i == 1:
        if idade < 20 and sexo == 'F':
            mu = mu+1
            nomemulheres = nome
        elif sexo == 'M':
            maioridade = idade
            nomemv = nome
    elif i == 2 or i == 3 or i == 4:
        if idade < 20 and sexo == 'F':
            mu = mu+1
            nomemulheres += ', '+ nome
        elif idade > maioridade and sexo == 'M':
            maioridade = idade
            nomemv = nome
    total += idade
if maioridade == 0:
    nomemv = nomemais
    maioridade = 'NENHUM'
print(f'A média das idades é {total/4}')
print(f'O nome do mais velho é {nomemv} e ele tem {maioridade} anos!')
print(f'Apenas {mu} mulheres tem menos que 20 anos.')
print(f'O nome delas é {nomemulheres}')