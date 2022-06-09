print('~'*30)
print('SEQUENCIA DE FIBONACCI!')
print('~'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} > {t2} ', end='')
while cont <= n:
    t3 = t1+t2
    print(f'> {t3} ', end='')
    cont += 1
    t1 = t2
    t2 = t3



#n= int(input("numero"))
#lista=[1,1]
#for i in range(n-2):
#      lista.append(lista[-1]+lista[-2])
#print(lista)