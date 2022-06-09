def cu(msg):
    num = len(msg) + 4
    print('~'* num)
    print(f'  {msg}')
    print('~'* num)


while True:
    cu(str(input('Digite uma mensagem: ')))