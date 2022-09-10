'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
while True:
    jogador = int(input("digite um valor:"))
    computador = randint(1,11)
    total = computador + jogador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("digite par ou impar: ")).strip().upper()[0]
    print(f"a soma do computador:{computador} e do jogador:{jogador} é {total} ", end="")
    print("e deu par" if total % 2 == 0 else "e deu impar")
    if tipo == "P":
        if total % 2 == 0:
            print("voçe ganhou!")
            v = v + 1
        else:
            print("voçe perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("voçe ganhou!")
            v = v + 1
        else:
            print("voçe perdeu!")
            break
print(f"voçe ganhou {v} vezes")