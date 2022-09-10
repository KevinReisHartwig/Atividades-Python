'''Exercício Python 54: Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
maior = 0
menor = 0

for i in range(1,4):
    ano = int(input(f"qual o ano de nascimento da {i}° pessoa: "))
    idade = atual - ano
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1



print("maior de idade {}".format(maior))
print("menor de idade {}".format(menor))