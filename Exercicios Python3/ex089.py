aluno = list()
classe = list()
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    classe.append(aluno[:])
    aluno.clear()
    while True:
        resp = str(input('Quer continuar?[S/N] '))[0].upper()
        if resp == 'N' or resp == 'S':
            break
    if resp == 'N':
        break
print(f'{"No.":<6}{"NOME":<12}{"MÉDIA":>6}')
for c in range(0, len(classe)):
    print(f'{c:<6}', end='')
    print(f'{classe[c][0]:<12}', end='')
    print(f'{(classe[c][1]+classe[c][2])/2:>6.2f}')
while True:
    opc = int(input('Quer mostrar as notas de qual aluno? Digite o "No." ou "999" para sair: '))
    if opc == 999:
        break
    print(f'Notas de {classe[opc][0]}!!!\nNota 1: {classe[opc][1]}\nNota 2: {classe[opc][2]}')