preco = float(input('Ganhe 5% de desconto. Digite o valor do seu produto: '))
desconto = (preco/100)*5
vcd = preco-desconto
print(f' De R${preco}, sairá por R${vcd}, economize já R${desconto}!')