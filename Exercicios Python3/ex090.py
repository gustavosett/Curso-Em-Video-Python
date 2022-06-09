aluno = dict()
aluno["nome"] = str(input('Nome: '))
aluno["nota"] = float(input('Média: '))

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
if aluno["nota"] < 6:
    print("Reprovado!")
elif aluno["nota"] >= 7:
    print('Aprovado!')
else:
    print('Recuperação')