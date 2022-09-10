'''12. Faça um software para calcular a distribuição de freqüência de 15 valores sorteados de 0 a 9.
Suponha os seguintes números sorteados: 4,5,7,8,9,1,8,2,4,3,2,5,6,7,0 Saída do programa:
Número 0: 1 vez
Número 1: 1 vez
Numero 2: 2 vezes
Número 3: 1 vez
Número 4: 2 vezes
Número 5: 2 vezes
Número 6: 1 vez
Número 7: 2 vezes
Numero 8: 2 vezes Número'''

import random
numeros = []
numero1 = 0
numero2= 0
numero3= 0
numero4 = 0
numero5 = 0
numero6= 0
numero7=0
numero8=0
numero9=0
numero0=0
for i in range(0,15):
    sorteio = random.randrange(0,9)
    numeros.append(sorteio)
print(numeros)
    if sorteio == 1:
        numero1 = numero1+ 1
        print('f')
    if sorteio == 2:
        numero2 = numero2+ 1
    if sorteio ==0:
        numero0 = numero0+ 1
    if sorteio ==3:
        numero3 = numero3+ 1
    if sorteio ==4:
        numero4 = numero4+ 1
    if sorteio ==5:
        numero5 = numero5+ 1
    if sorteio == 6:
        numero6 = numero6+ 1
    if sorteio == 7:
        numero7 = numero7+ 1
    if sorteio == 8:
        numero8 = numero8+ 1
    if sorteio ==9:
        numero9= numero9+ 1



