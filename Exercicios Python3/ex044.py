valor = float(input('Qual o valor do produto em R$? '))
pagamento = str(input('Qual a forma de pagamento? Dinheiro, cheque ou cartão? ')).upper()
if pagamento == "CARTÃO":
    vezes = int(input('Quantas vezes? '))
    if vezes > 10:
        print('Só fazemos em até 10x!')
    elif vezes < 3:
        print(f'Pronto, compra efetuada em {vezes}x de R${valor/vezes:.2f}')
    else:
        print(f'Pronto, compra efetuada em {vezes}x de R${(((valor/100)*30)+valor)/vezes:.2f}')
elif pagamento == 'DINHEIRO' or pagamento == 'CHEQUE':
    print(f'Você ganha um desconto de R${(valor/100)*10:.2f} e valor do produto sai por R${valor - ((valor/100)*10):.2f}')
else:
    print('Desculpa, não entendi.')