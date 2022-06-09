peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em cm? '))
IMC = peso / (altura/100)**2
if IMC < 18.5:
    print(f'Você tem um IMC de {IMC:.2f} e está abaixo do peso!')
elif IMC > 18.5 and IMC < 25:
    print(f'Você tem um IMC de {IMC:.2f} e está no peso ideal!')
elif IMC > 25 and IMC < 30:
    print(f'Você tem um IMC de {IMC:.2f} e está acima do peso!')
elif IMC > 30 and IMC < 40:
    print(f'Cuidado, você tem um IMC de {IMC:.2f} e está obeso!')
else:
    print(f'Procure um médico ou nutricionista urgente, você tem um IMC de {IMC:.2f} e está em obesidade mórbita!')