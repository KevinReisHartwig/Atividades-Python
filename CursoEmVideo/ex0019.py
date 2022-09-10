'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
n1 = input("digite o primeiro nome: ")
n2 = input("digite o segundo nome: ")
n3 = input("digite o terceiro nome: ")
n4 = input("digite o quarto nome: ")
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print("o escolhido foi {}".format(escolhido))