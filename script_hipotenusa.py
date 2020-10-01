#!/usr/bin/env python3
import sys
import math

#Associando os dados que serão colocados na linha de comando a variáveis e transformando-os em inteiros.

number1 = int(sys.argv[1]) 
number2 = int(sys.argv[2])

#Utilizando o comando isinstance para confirmar que as variáveis se tratam de números inteiros após a transformação acima.

print(isinstance(number1, int))
print(isinstance(number2, int))

#Utilizando o comando if para garantir que o cálculo só será realizado se as variáveis forem positivas (<= 0) e menores que 1000 e printando a resposta no caso do cálculo com a hipotenusa abreviada para duas casas depois da vírgula. Caso o valor não atinja as condições, diz-se que as variáveis não atendem os requisitos.

if 0 <= number1 < 1000 and 0 <= number2 < 1000:
	hip = math.sqrt((number1**2) + (number2**2))
	print('O quadrado da hipotenusa do triângulo retângulo com os lados a = {0} e b = {1}, é {2}.'.format(number1, number2, round( hip, 2)))
else:
	print('As variáveis não atendem os requisitos!')


