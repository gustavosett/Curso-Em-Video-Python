import time
import random
cor = {'limpa':'\033[m',
       'amarelo':'\033[33m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'ciano':'\033[36m'}

print('-='*20)
print('JO KEN PÔ!')
print('-='*20)
escolha = str(input(f"Escolha {cor['amarelo']}PEDRA{cor['limpa']}, "
                    f"{cor['vermelho']}PAPEL{cor['limpa']} "
                    f"ou {cor['verde']}TESOURA{cor['limpa']}! ")).upper()
ppt = ['PEDRA', 'PAPEL', 'TESOURA']
ia_escolha = random.choice(ppt)
print(f"{cor['ciano']}CONTANDO RESULTADOS...{cor['limpa']}")
time.sleep(1)
print('.')
time.sleep(0.5)
print('..')
time.sleep(0.5)
print('...')
time.sleep(0.5)
if escolha == 'PEDRA' and ia_escolha == 'PEDRA'\
        or escolha == 'PAPEL' and ia_escolha == 'PAPEL'\
        or escolha == 'TESOURA' and ia_escolha == 'TESOURA':
    print(f"{cor['amarelo']}Você escolheu {escolha} e a máquina escolheu {ia_escolha}! EMPATOU!{cor['limpa']}")
elif escolha == 'PEDRA' and ia_escolha == 'PAPEL' \
        or escolha == 'PAPEL' and ia_escolha == 'TESOURA' \
        or escolha == 'TESOURA' and ia_escolha == 'PEDRA':
    print(f"{cor['vermelho']}Você escolheu {escolha} e a máquina escolheu {ia_escolha}! VOCÊ PERDEU!{cor['limpa']}")
elif escolha == 'PEDRA' and ia_escolha == 'TESOURA' \
        or escolha == 'PAPEL' and ia_escolha == 'PEDRA' \
        or escolha == 'TESOURA' and ia_escolha == 'PAPEL':
    print(f"{cor['verde']}Você escolheu {escolha} e a máquina escolheu {ia_escolha}! VOCÊ GANHOU!!{cor['limpa']}")
else:
    print(f"{cor['vermelho']}Desculpa, não entendi! :({cor['limpa']}")