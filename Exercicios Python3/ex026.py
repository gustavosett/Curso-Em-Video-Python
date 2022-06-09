string = str(input('Digite um nome: ')).lower().strip().replace(" ", "")
print(f'A letra A aparece {string.count("a")} vezes!')
print(f'A primeira letra A aparece na {string.find("a")+1}ª letra!')
print(f'E a última letra A aparece na {string.rfind("a")+1}ª letra!')
