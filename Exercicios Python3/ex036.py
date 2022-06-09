import time
vcasa = float(input('Qual o valor da casa em R$: '))
salario = float(input('Qual o valor do seu salário: '))
ano = int(input('Quantos anos você vai pagar sua divida?'))
anos = ano * 12
imprestimo = vcasa/anos
imprestimo_abusivo = vcasa/(anos*2)
if (salario/100)*30 < imprestimo*2:
    print('Infelizmente o valor do imprestimo que você quer fazer, corresponde a mais de 30% do seu salário!')
    print('...')
    time.sleep(5)
    print(f'\033[36mMas se eu conversar com o gerente aqui, talvez consiga fazer por R$ {imprestimo_abusivo*3.5:.2f} em {ano*2} anos...\033[m')

else:
    print(f'\033[95mVerificamos que é possível estar fazendo o financiamento da sua casa,\no valor da sua parcela sairá por apenas R${(imprestimo*2):.2f}!\033[m')