cor = { 'vermelho':'\033[31m',
         'verde':'\033[32m',
         'limpa':'\033[m', }
import random
escolhas = [0, 5]
while True:
    ia_escolha = random.randint(0, 5)
    jg_escolha = str(input('PAR OU IMPAR! ')).upper()
    jg_numero = int(input('DIGITE NÚMERO DE 0 A 5: '))
    if jg_escolha == 'PAR' and ((jg_numero+ia_escolha)%2 == 0):
        break
    elif jg_escolha == 'IMPAR' and ((jg_numero+ia_escolha)%2 == 1):
        break
    elif jg_escolha == 'PAR' and ((jg_numero+ia_escolha)%2 == 1):
        print(f'{cor["vermelho"]}Você perdeu! o resultado foi IMPAR! '
                              f'{jg_numero} + {ia_escolha} = {jg_numero+ia_escolha}!!{cor["limpa"]}')
    else:
        print(f'{cor["vermelho"]}Você perdeu! o resultado foi PAR!'
              f' {jg_numero} + {ia_escolha} = {jg_numero + ia_escolha}!!{cor["limpa"]}')
print(f'{cor["verde"]}Parabéns você ganhou! O resultado foi {jg_escolha}!!'
      f' {jg_numero} + {ia_escolha} = {jg_numero+ia_escolha}!!')