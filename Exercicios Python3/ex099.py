from random import randint
def randomlist(a):
    a = []
    for i in range(0, randint(0, 10)):
        num = randint(0, 20)
        a.append(num)
    print(f'\033[33mLista:\033[m{a}')
    if a == []:
        print(f'\033[31mA lista não tem nenhum número.\033[m')
    else:
        print(f'\033[36mO maior número da lista foi \033[m{max(a)}')


for i in range(0, randint(1, 10)):
    randomlist(i)