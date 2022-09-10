'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint # numero aleatorio
from time import sleep # fazer pausa
computador = randint(0,5) # pensar em um numero de 0 a 5
print("-=-"* 20)
print("vou pensar em um numero de 0 a 5, tente adivinhar!")
print("-=-"* 20)
jogador = int(input("digite um numero: "))
print("processando...")
sleep(3)
if jogador == computador:
    print("você acertou o numero parabens!")
else:
    print("você errou! o numero era {}".format(computador))
