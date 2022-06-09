def aumentar (preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir (preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda="R$"):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, aum=10, dim=20):
    print(f'Preço analisado: \t{moeda(preço)}\n'
          f'Dobro do preço: \t{dobro(preço, True)}\n'
          f'Metade do preço: \t{metade(preço, True)}\n'
          f'{aum}% de aumento: \t{aumentar(preço, aum, True)}\n'
          f'{dim}% de redução: \t{diminuir(preço, dim, True)}\n')