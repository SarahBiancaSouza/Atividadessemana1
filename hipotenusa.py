import math
cateto_oposto = int(input('Qual o valor do cateto oposto?'))
cateto_adjacente = int(input('Qual o valor do cateto adjacente?'))

hipotenusa = (cateto_adjacente**2) + (cateto_oposto**2)
raiz_quadrada = math.sqrt(hipotenusa)
print(raiz_quadrada)