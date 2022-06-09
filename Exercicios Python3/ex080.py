listanum = []
for c in range(0, 5):
    while True:
        valor = int(input('Digite um valor: '))
        if valor not in listanum:
            listanum.append(valor)
            break
        else:
            print('Número inválido.')
    if c == 0:
        print('Criando lista...')
    else:
        listanum = sorted(listanum)
        if valor == (min(listanum)):
            print('Adicionado ao começo da lista.')
        elif valor == (max(listanum)):
            print('Adicionado ao final da lista.')
        else:
            print(f'Adicionado na posição {listanum.index(valor)} da lista.')
print(f'Aqui está sua lista em ordem {listanum}')