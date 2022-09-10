'''Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''
n = int(input("digite um numero: "))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print("o numero {} tem como dobro {}, triplo é {} e raiz quadrada é {}".format(n, dobro, triplo, raiz))