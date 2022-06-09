import sistema
from sistema.cadastros import *


class Cadastro:

    def __int__(self):
        cadastro = {}
        arq = 'cadastros.txt'


    def arquivoExiste(arq):
        try:
            a = open(arq, 'rt')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True


    def criarArquivo(nome):
        try:
            a = open(nome, 'wt+')
            a.close()
        except:
            print('erro criar arquivo.')
        else:
            print(f'Arquivo {nome} criado com sucesso!')


    def menucadastro(msg = 'PESSOAS CADASTRADAS'):
        if not arquivoExiste(arq):
            criarArquivo(arq)
        num = len(msg) + 16
        print('-'* num)
        print(f'{msg:^30}')
        print('-'* num)
        a = open(arq, 'rt')
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'Nome: {dado[0]}        \tIdade: {dado[1]} \tSexo: {dado[2]}')
        while True:
            resp = str(input('Digite "0" para voltar para o menu: '))[0].upper()
            if resp == "0":
                break
            else:
                print("Apenas o número 0!!")
        if resp == "0":
            a.close()
            return sistema.menu()


    def cadastrorapido():
        while True:
            try:
                a = open(arq, 'at')
                nome = str(input("Nome: "))
                idade = int(input("Idade: "))
                sexo = str(input("Sexo[M/F]: "))[0].upper()
            except:
                print("ERRO!")
            else:
                a.write(f'{nome};{idade};{sexo}\n')
                print("cadastrado com sucesso!")
                while True:
                    resp = str(input("Quer cadastrar mais alguém?[S/N]: "))[0].upper()
                    if resp == "S" or resp == "N":
                        break
                    else:
                        print("Apenas S ou N!!!")
                if resp == "N":
                    a.close()
                    return sistema.menu()
