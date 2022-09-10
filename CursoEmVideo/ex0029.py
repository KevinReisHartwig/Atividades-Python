'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
from time import sleep
km = float(input("digite quantos km/h o carra esta fazendo : "))
if km > 80:
    print("mutado! você estava acima da velocidade que é 80 k/h")
    multa = (km-80) * 7
    print("calculando sua multa!")
    sleep(3)
    print("você vai ter que pagar uma multa de R${:.2f}".format(multa))
else:
    print("tenha um boa dia dirija com segurança!")