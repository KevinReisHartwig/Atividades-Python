'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
menor = 0
maior = 0

for i in range(1,6):
    peso = float(input("qual o peso da {}° pessoa: ".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("o maior peso é {}".format(maior))
print("o menor peso é {}".format(menor))