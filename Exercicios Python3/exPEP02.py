def RetiraLetra(string, num, num2=False):
    string = list(string)
    if num2:
        for i in range(num, num2):
            del (string[num])
    else:
        del (string[num])
    return "".join(string)


frase = "Chaveiro"
letranum = 4
letranum2 = 8

print(RetiraLetra(frase, letranum, letranum2))
