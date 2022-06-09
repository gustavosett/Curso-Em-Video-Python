palavra = ('sexo', 'travesti', 'sonegação', 'pcgamer', 'ronaldinho', 'pendrive', 'samba', 'porno', 'incesto',
           'pau', 'duro', 'infertilidade', 'tiktok', 'jogodobixo', 'macaco', 'assassinato', 'freefire')
for p in palavra:
    print(f'\nNa palavra \033[33m{p.upper()}\033[m temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': print(f'\033[33m{letra}\033[m', end=' ')