'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(* num):
    cont = maior = 0
    print("=-"*30)
    print("analisando valores... ")
    for valor in num:
        print(f"{valor} ",end="",flush=True)
        sleep(0.3)
        if cont ==0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont +1
    print(f"foram informados {cont} valores ao todo")
    print(f"o maior valor é {maior}")

maior(2,5,7,4,9,3)
maior()
maior(9)
maior(6,4,3)
