from sistema import cadastros


def menu(msg = 'MENU PRINCIPAL'):
    num = len(msg) + 16
    print('-'* num)
    print(f'{msg:^30}')
    print('-'* num)
    print(f'''1 - Ver pessoas cadastradas
              2 - Casdastrar nova pessoa
              3 - Sair do Sistema ''')
    return resp(int(input(f"Sua Opção: ")))


def resp(num):
    while True:
        if num == 1:
            cadastros.menucadastro()
            break
        elif num == 2 :
            cadastros.cadastrorapido()
            break
        elif num == 3:
            print(f"obrigado e volte sempre!")
            exit(0)
        else:
            print(f"Digite uma opção válida!")
            num = str(input(f"Sua opção: "))


def start():
    menu()