opcao = 0
while opcao != 5:
    pv = int(input('Digite o primeiro valor: '))
    sv = int(input('Digite o segundo valor: '))
    print('     [ 1 ] somar\n     [ 2 ] multiplicar'
          '\n     [ 3 ] maior\n     [ 4 ] novos números'
          '\n     [ 5 ] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'{pv} + {sv} = {pv+sv}')
    elif opcao == 2:
        print(f'{pv} X {sv} = {pv*sv}')
    elif opcao == 3:
        if pv > sv:
            print(f'{pv} é maior que {sv}!!')
        elif pv < sv:
            print(f'{sv} é maior que {pv}!!')
        else:
            print(f'{pv} e {sv} são iguais!!')
    elif opcao == 4:
        print('Quais são os números novamente?')
print('Obrigado e volte sempre!')