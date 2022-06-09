sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Não entendi, qual o seu sexo? [M/F] '))[0].upper().strip()
if sexo == 'M':
    sexo = 'masculino'
else:
    sexo = 'feminino'
print(f'Entendi, seu sexo é {sexo}!')