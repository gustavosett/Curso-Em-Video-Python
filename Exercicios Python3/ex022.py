nome = str(input('Digite seu nome completo: '))

maiusculas = nome.upper(); minusculas = nome.lower()
contagem1 = len(nome) - nome.count(' ')
contagem2 = nome.find(' ')

print(f'''Seu nome em maiusculas é {maiusculas}.
Seu nome em minusculas é {minusculas}.
Seu nome tem ao todo {contagem1} letras.
E seu primeiro nome tem {contagem2} letras.''')