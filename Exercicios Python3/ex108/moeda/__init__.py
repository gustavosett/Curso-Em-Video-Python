def metade(num):
    met = num / 2
    return f'{met:1f}'.replace(".", ",")


def dobro(num):
    met = num * 2
    return f'{met:1f}'.replace(".", ",")


def porcen(num):
    met = (num/100)*10
    met += num
    return f'{met:1f}'.replace(".", ",")


