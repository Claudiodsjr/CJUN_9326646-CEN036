#!/usr/bin/env python3
import sys
import math

#Começo avaliando se as variáveis são numéricas ou não. Se forem numéricas sigo para a transformação destas em inteiros e então a avaliação se são positivas e menores que 1000, caso atinjam estas condições, faço o calculo da hipotenusa, caso não atinjam, digo que as variáveis não atendem a necessidade de serem positivas e/ou menores que 1000. Caso não sejam números, aviso que as variáveis não são numéricas.

if sys.argv[1].isdigit() == True and sys.argv[2].isdigit() == True:
	number1 = int(sys.argv[1]) 
	number2 = int(sys.argv[2])
	print('As variáveis são numéricas.')
	print('A primeira variável é um número inteiro?', isinstance(number1, int))
	print('A segunda variável é um número inteiro?', isinstance(number2, int))
	if 0 <= number1 < 1000 and 0 <= number2 < 1000:
		hip = math.sqrt((number1**2) + (number2**2))
		print('O quadrado da hipotenusa do triângulo retângulo com os lados a = {0} e b = {1}, é {2}.'.format(number1, number2, round(hip, 2)))
	else:
		print('As variáveis não atendem aos requisitos!')
else:
	print('Variáveis não numéricas, não inteiras ou negativas.')


