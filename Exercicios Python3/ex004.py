cor = {'limpa':'\033[m',
       'azul':'\033[34m',
       'ciano':'\033[36m',
       'rosa':'\033[95m'}
string=input('Digite algo.')
string.isnumeric()
print(f'{cor["ciano"]}Está string é númerica? {string.isnumeric()}{cor["limpa"]}')
print(f'{cor["rosa"]}Está string é alfanumérica? {string.isalnum()}{cor["limpa"]}')
print(f'{cor["azul"]}Está string é alfabética? {string.isalpha()}')
print(f'Está string é um código ASCII? {string.isascii()}')
print(f'Está string é está em caixa alta? {string.isupper()}')