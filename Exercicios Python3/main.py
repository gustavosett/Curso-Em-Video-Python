def traço():
    traco = ("* " + ("- " * 4)) * 2 + "*"
    return print(traco)


def bordas():
    borda = "|" + " " * 9
    for b in range(0, 4):
        print((borda * 3).strip())

def casa():
    for i in range(0, 1):
        traço()
        bordas()
    traço()

casa()