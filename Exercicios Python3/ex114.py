from socket import gethostbyname

try:
    host = str(input("Veja se o site está disponível: www."))
    print("solucionando ...")
    ip = gethostbyname(host)
except:
    print(f'O site {host} está offline!')
else:
    print(f'O site {host} é acessível com IP: {ip}')