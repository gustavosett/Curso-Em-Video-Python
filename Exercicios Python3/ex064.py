cont = num = conta = 0
while num != 999:
    num = int(input('Digite um número [999 para parar] '))
    if num != 999:
        conta += num
        cont += 1
print(f'{cont} números e o total da soma foi {conta}!')