import math
cate1 = float(input('Digite o cateto adjacente em m²: '))
cate2 = float(input('Pronto, agora o cateto oposto em m²: '))
hipo= math.hypot(cate1, cate2)
area = (cate1*cate2)/2
print(f'A hipotenusa é: {hipo:.2f}m², e sua área é {area:.2f}m²!')