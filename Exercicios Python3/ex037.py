num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
      [ 1 ] Converter para BINÁRIO.
      [ 2 ] Converter para OCTAL.
      [ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para binário é {bin(num)}.')
elif opção == 2:
    print(f'{num} convertido para octal é {oct(num)}.')
elif opção == 3:
    print(f'{num} convertido para hexadecimal é {hex(num)}.')
else:
    print('Desculpa não entendi. :(')