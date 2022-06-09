nome = input('Qual seu nome? ')
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome in 'João Pedro Luana Fernando':
    print('Seu nome é bem popular no Brasil!')
elif nome == 'Pedrinho Matador':
    print('A policia já está vindo!')
else:
    print('Seu nome é bem normal!')
print(f'Bom dia, {nome}!')
