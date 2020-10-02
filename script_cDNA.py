#!/usr/bin/env python3
import sys

#Criando as 5 variáveis dos 5 argumentos utilizados, sendo eles a sequência e as CDS buscadas nesta sequência.

dnas = str(sys.argv[1])
if sys.argv[2].isdigit() == True and sys.argv[3].isdigit() == True and sys.argv[4].isdigit() == True and sys.argv[5].isdigit() == True:
	n1 = int(sys.argv[2])
	n2 = int(sys.argv[3])
	n3 = int(sys.argv[4])
	n4 = int(sys.argv[5])
	print('As estradas numéricas estão corretas!')
else:
	print('Ao menos uma das variáveis que deveriam ser numéricas, não é, confira e tente novamente.')

print('##############################################################')

#Conferindo se os dados passados são do tipo correto com o comando insinstance() e conferindo se os números inteiros não são maiores do que a sequência de DNA. 

print('Avaliação dos tipos de variáveis:')

print('A primeira variável é um string?', isinstance(dnas, str))
print('A segunda variável é um número inteiro?', isinstance(n1, int))
print('A terceira variável é um número inteiro?', isinstance(n2, int))
print('A quarta variável é um número inteiro?', isinstance(n3, int))
print('A quinta variável é um número inteirow', isinstance(n3, int))

print('##############################################################')

count = len(dnas)

print('Verificação se as variáveis numéricas se encontram dentro do limite de componentes da sequência:')

if n1 <= count and n2 <= count and n3 <= count and n4 <= count:
	print('As variáveis {0}, {1}, {2} e {3} são menores que a sequência, que possui um total de {4} componentes.'.format(n1, n2, n3, n4, count))
else:
	print('Pelo menos uma das variáveis ({0}, {1}, {2}, {3}) possui valor maior que o limite da sequência ({4})!'.format(n1, n2, n3, n4, count))

print('##############################################################')

#Extraindo a sequência CDS 1 e conferindo se inicia com o códon ATG, lembrando que como a contagem se inicia no 0, se a cordenada começa no 20, inciaindo no 1, temos que ustilizar 19 quando inicia no 0.

cds1 = dnas[(n1 - 1):(n2 - 1)]

print('A sequência CDS 1 é: {0}!'.format(cds1))

if cds1[:3] == 'ATG':
	print('O códon de início de CDS1 é ATG.')
else:
	print('O códon de início de CDS1 não é ATG, ele é {0}.'.format(cds1[:3]))

print('##############################################################')

#Extraindo a sequência CDS 2 e conferindo se termina com um dos códons de parada, TAG, TAA ou TGA.

cds2 = dnas[(n3 - 1):(n4 - 1)]
print('A sequência CDS 2 é: {0}'.format(cds2))

if cds2[-3:] == 'TAG':
	print('A sequência CDS 2 termina com o códon {0}, que é um dos três possíveis (TAG, TAA ou TGA).'.format(cds2[-3:]))
elif cds2[-3:] == 'TAA':
	 print('A sequência CDS 2 termina com o códon {0}, que é um dos três possíveis (TAG, TAA ou TGA).'.format(cds2[-3:]))
elif cds2[-3:] == 'TGA':
	 print('A sequência CDS 2 termina com o códon {0}, que é um dos três possíveis (TAG, TAA ou TGA).'.format(cds2[-3:]))
else:
	print('A sequência CDS 2 não termina com nenhuma das três opções de códon, ela termina com o códon {0}.'.format(cds2[-3:]))

print('##############################################################')

