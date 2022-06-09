while True:
    try:
        num1 = int(input("Digite um número inteiro: "))
    except:
        print("Digite um número inteiro válido!")
    else:
        break
while True:
    try:
        num2 = float(input("Digite um número real: "))
    except:
        print("erro, digite um numero real válido!")
    else:
        break
print(f"O valor inteiro digitado foi {num1} e o real foi {num2:.1f}")