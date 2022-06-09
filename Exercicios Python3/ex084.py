cadastro = list()
pessoa = list()
mai = men = 0
nmai = list()
nmen = list()
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if len(cadastro) == 0:
        mai = men = pessoa[1]
    else:
        if mai < pessoa[1]:
            mai = pessoa[1]
        if men > pessoa[1]:
            men = pessoa[1]
    cadastro.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Você quer continuar?[S/N] '))[0].upper()
    if resp == 'N':
        break
for p in cadastro:
    if p[1] == mai:
        nmai.append(p[0])
    if p[1] == men:
        nmen.append(p[0])
print(f'Ao todo você cadastrou {len(cadastro)} pessoas!')
print(f'O maior peso foi de {mai}KG. Peso de {nmai}')
print(f'O menor peso foi de {men}KG. Peso de {nmen}')