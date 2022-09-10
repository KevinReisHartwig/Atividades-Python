'''10)Escrever um algoritmo que lê um valor n e outro valor m, e calcula a tabuada de n de
1 até m.'''

numero = int(input("digite um numero inteiro para fazer sua tabuada:" ))
for n in range(1, 11):
    print("{} x {} = {}".format(numero, n, numero*n))
