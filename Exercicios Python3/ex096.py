def area(a, b):
    s = a*b
    print(f'A area de um terreno de {a}m x {b}m é {s:.2f}m².')


largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento(m): '))
area(largura, comprimento)