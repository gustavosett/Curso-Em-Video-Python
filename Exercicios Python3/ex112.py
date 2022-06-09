from UcV import moeda


preco = str(input("preço: R$")).replace(",", ".")

if preco.isalpha():
    print(F'ERRO: "{preco}" é um preço inválido!')
else:
    moeda.resumo(float(preco), 10, 20)