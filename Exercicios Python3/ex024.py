cidade = str(input('Qual cidade que você nasceu?')).upper().strip().replace(" ", "").split()
print('Você nasceu em Araçatuba?{}'.format('ARAÇATUBA' in cidade))

