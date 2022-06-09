import math

largura = float(input('Quantos metros tem a largura da sua parede?'))
altura = float(input('Quantos metros tem a altura da sua parede?'))
calc = (largura * altura)
area = math.sqrt(calc)
latas = (area / 2)
print(f'Sua área é {area:.2f}m², e você ira precisar de {latas:.1f} latas de tinta.')