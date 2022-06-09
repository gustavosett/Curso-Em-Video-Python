cliente = str(input('Faça já seu cambio! Quantos reais você deseja converter? '))

cotacao = 5.25
x = cliente.replace('R$', '')
cliente1 = float(x)
if isinstance(cliente1, float):
    dolar = cliente1 / cotacao



    print(f'Parabéns, compra conclúida!\n Você comprou {dolar:.2f} dólares.')