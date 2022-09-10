'''Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

n = int(input("digite um numero inteiro: "))
if n % 2 != 0:
    print("é impar")
else:
    print("par")