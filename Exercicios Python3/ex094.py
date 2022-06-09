pessoa = dict()
cadastro = list()
muie = list()
medidade = 0
nome = str
velho = list()
while True:
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa["sexo"] = str(input('Sexo[M/F]: '))[0].upper()
        if pessoa["sexo"] == "M":
            break
        elif pessoa["sexo"] == 'F':
            nome = pessoa["nome"]
            muie.append(nome)
            break
        else:
            print('Por favor, apenas M ou F.')
    pessoa["idade"] = int(input("Idade: "))
    medidade += pessoa["idade"]
    cadastro.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar?[S/N]"))[0].upper()
        if resp == "S" or resp == "N":
            break
        else:
            print("Por favor, apenas S ou N!")
    if resp == "N": break
mediaidade = medidade/(len(cadastro))
for k, v in enumerate(cadastro):
    if v['idade'] > mediaidade:
        velho.append(v['nome'])
print(f'''
A) Ao todo temos {len(cadastro)} pessoas cadastradas.
B) A média de idade é de {mediaidade:.2f} anos. 
C) As mulheres cadastradas foram a {', '.join(muie)}.
D) Lista das pessoas mais velhas que a média: {', '.join(velho)}
''')