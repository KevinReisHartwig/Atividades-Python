'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
ai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também
deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date

atual = date.today().year

ano = int(input("informe o ano que voce nasceu: "))

idade = atual - ano

print("você nasceu em {} e o ano atual é {}, então você tem {} de idade".format(ano,atual, idade))
saldo = idade - 18
alistamento = atual - saldo
if idade == 18:
    print("você completou {} e tem que se alistar para o serviço militar!".format(idade))
elif idade < 18:
    print("você tem {} e ainda não tem 18 anos para se alistar ao serviço militar!".format(idade))
else:
    print("você já deveria ter se alistado {} anos atras, tem {} anos de idade".format(saldo,idade))
    print("seu alistamento se ocorreu foi em {}".format(alistamento))