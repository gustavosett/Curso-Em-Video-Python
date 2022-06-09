import random;
frase = 'oi, eu sou o Gustavo';
lista = frase.split(); random.shuffle(lista);
print(lista)


#len(frase) mostra quantos caracteres tem dentro da string.
#frase.count('o') vai me contrar, quantas vezes a letra "o" aparece.
#frase.count('o,0,13')vai contar até onde fatiou
#frase.find('Gustavo') vai me apontar o numero 13, onde começa a palavra procurada.
#frase.replace(oi, tchau) ira trocar.
#frase.upper ira jogar tudo para maisculo e .lower faz o contrário.
#frase.capitalize() deixando só o primeiro caractere em maiúsculo.
#frase.title() transforma todas as primeiras letras de cada palavra em letra maiúscula.
#frase.strip() proteção contra velho, remove todos os espaços no inicio e no fim da string
#usando o "r" de right ou "l" de left ex .rstrip() faz apagar apenas os espaços da direita.
#Divisão
#frase.split() em base gera uma lista com todas as palavras da string, portanto esse comando há uma infinidade de
#utilizações extremamente úteis e é recomendável ser estudado individualmente.
#Junção
#''.join(frase) o join junta toda uma string ou lista em só um texto continuo separado por tudo que estiver dentro
#das aspas ''. Ou seja traços '-', espaços ' ' ou absolutamente nada ''.
#Ex oi,eusouoGustavo ou oi,-eu-sou-o-Gustavo