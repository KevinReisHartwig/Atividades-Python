'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

nome = input("digite seu nome: ").strip()
print("analisando o nome...")
print("seu nome com letras maisculas é {}".format(nome.upper()))
print("seu nome com letras minusculas é {}".format(nome.lower()))
print("seu nome tem quantas letras? {} ".format(len(nome) - nome.count(' ')))
separa = nome.split()
print("seu primeiro nome {} tem {} letras".format(separa[0], len(separa[0])))

