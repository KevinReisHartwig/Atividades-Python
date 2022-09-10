'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
 formar um triângulo.'''
n1 = float(input("digite o primeiro segmento: "))
n2 = float(input("digite o segundo segmento: "))
n3 = float(input("digite o terceiro segmento: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("os segmentos formam um triangulo")
else:
    print("não forma um triangulo")