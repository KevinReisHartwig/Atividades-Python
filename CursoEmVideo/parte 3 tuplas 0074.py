'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

Aula Anterior'''
from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print("os valores sorteados foram ", end='')
for n in numeros:
    print(f"{n} ", end="")
print(f"\no maior numero foi {max(numeros)}")
print(f"o menor numero foi {min(numeros)}")