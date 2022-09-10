'''Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
from datetime import date
ano = int(input("qual ano você quer analisar? "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("{}, ele é bissesto".format(ano))
else:
    print("{}, não é bissesto".format(ano))