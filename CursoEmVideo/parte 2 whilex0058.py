'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint # numero aleatorio
from time import sleep # fazer pausa
palpites = 0
computador = randint(0,10) # pensar em um numero de 0 a 5
print("-=-"* 20)
print("vou pensar em um numero de 0 a 10, tente adivinhar!")
print("-=-"* 20)
acertou = False

while not acertou:
    jogador = int(input("qual seu palpite de 1 a 10: "))
    palpites = palpites + 1
    print("processando...")
    sleep(1)
    if jogador == computador:
        acertou = True

    else:
        if jogador < computador:
            print("errou é mais")
        elif jogador > computador:
            print("errou é menos")


print("você acertou o numero parabens e errou {} vezes!".format(palpites))







