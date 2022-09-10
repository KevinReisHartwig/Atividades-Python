'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

primeiro = int(input("digite o primeiro termo: "))
razão = int(input("digite a razão: "))
decimo = primeiro + (10-1)* razão
for i in range(primeiro,decimo,razão):
    print(i,end=' --> ')