num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 < num2:
    print(f'O número {num1}, é menor que {num2}!')
elif num1 > num2:
    print(f'O número {num2}, é menor que {num1}!')
else:
    print(f'Os números {num1} e {num2}, são iguais!')