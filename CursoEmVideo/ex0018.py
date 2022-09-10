'''Exercício Python 18: Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import radians, sin, cos , tan
angulo = float(input("digite o angulo que você deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("o angulo {:.2f} tem o seno {}".format(angulo, seno))
print("o angulo {:.2f} tem o cosseno {}".format(angulo, cosseno))
print("o angulo {:.2f} tem a tangente {}".format(angulo, tangente))