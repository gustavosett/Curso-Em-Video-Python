import unidecode
string_velha = str(input('Digite um palíndromo! ')).lower().replace(' ','')
string_nova = unidecode.unidecode(string_velha).replace('.','').replace(',','')
if string_nova[::-1] == string_nova:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')



#cagaram na minha cabeça com esse daqui
#string = str(input('Digite um palíndromo! '))[::-1]
#print(string)