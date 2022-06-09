nome = str(input('Digite seu nome: ')).title().strip()
pnome = nome[0:(int(nome.find(' ')))]
unome = nome[(int(nome.rfind(' '))):(int(len(nome)+1))]
print(f'''Muito prazer!
Seu primeiro nome é {pnome}!
E o seu último nome é {unome}!''')