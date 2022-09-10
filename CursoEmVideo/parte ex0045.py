'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep
itens = ("pedra","papel","tesoura")
computador = randint(0,2)
print("=-"*11)
print('''opções:
[0] Pedra
[1] Papel
[2] tesoura''')
jogador = int(input("qual sua opção:"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(1)
print("=-"*11)

print("O computador jogou {}".format(itens[computador]))
print("-="*11)
if jogador > 2:
    print("jogada invalida!")
print("O jogador jogou {}".format(itens[jogador]))

print("-="*11)
if computador == 0:
    if jogador ==0:
        print("empate")
    elif jogador == 1:
        print("jogador venceu")
    elif jogador == 2:
        print("computador venceu")
    else:
        print("numero invalido!")
elif computador == 1:
    if jogador == 0:
        print("computador venceu")
    elif jogador == 1:
        print("empate")
    elif jogador == 2:
        print("jogador venceu")
elif computador == 2:
    if jogador == 2:
        print("empate")
    elif jogador == 0:
        print("jogador venceu")
    elif jogador == 1:
        print("computador venceu")
else:
    print("jogada invalida!")
