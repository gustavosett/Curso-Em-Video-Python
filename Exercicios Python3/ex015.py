dias = int(input('Quantos dias alugado?'))
km = int(input('Quantos km rodados?'))
pago = (dias*60) + (km*0.15)
print(f'Você tem que pagar R${pago:.2f} AGORA!')